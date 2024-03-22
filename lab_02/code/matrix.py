from random import randint
from constants import *

class Matrix():
    def __init__(self, n, m):
        self.__n, self.__m = n, m
        self.create_matrix()

    def create_matrix(self):
        self.matrix = [[0] * self.__m for i in range(self.__n)]

    def output_matrix(self):
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.matrix[i][j], end=' ')
            print()
        print()

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def get_size(self):
        return self.__n, self.__m

    def fill_matrix_random_values(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.matrix[i][j] = randint(MIN_RAND, MAX_RAND)

def input_size_matrixes():
     size = input('Введите размер матрицы А через пробел: ')
     

def multiply_matrixes_ordinary(matrix_a, matrix_b) -> list[list[int]]:
    n, m = matrix_a.get_size()
    q, p = matrix_b.get_size()
    if m != q:
        print('Несовпадение размеров матриц')
        return
    else:
        matrix_result = Matrix(n, p)
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    matrix_result[i][j] = matrix_result[i][j] + matrix_a[i][k] * matrix_b[k][j]
        return matrix_result

def multiply_matrixes_vinograd(matrix_a, matrix_b) -> list[list[int]]:
    n, m = matrix_a.get_size()
    q, p = matrix_b.get_size()
    if m != q:
        print('Несовпадение размеров матриц')
        return
    else:
        matrix_result = Matrix(n, p)
        d = int(m / 2)
        mul_u = [0] * n
        for i in range(n):
            for j in range(d):
                mul_u[i] = mul_u[i] + matrix_a[i][2*j] * matrix_a[i][2*j + 1]

        mul_w = [0] * p
        for i in range(p):
            for j in range(d):
                mul_w[i] = mul_w[i] + matrix_b[2*j][i] * matrix_b[2*j + 1][i]

        for i in range(n):
            for j in range(p):
                matrix_result[i][j] = -mul_u[i] - mul_w[j]
                for k in range(d):
                    matrix_result[i][j] = matrix_result[i][j] + (matrix_a[i][2*k] + matrix_b[2*k+1][j]) * \
                                                                (matrix_a[i][2*k+1] + matrix_b[2*k][j])
                                                    
        if m % 2 == 1:
            for i in range(n):
                for j in range(p):
                    matrix_result[i][j] = matrix_result[i][j] + matrix_a[i][m-1] * matrix_b[m-1][j]

        return matrix_result

def multiply_matrixes_vinograd_optimized(matrix_a, matrix_b) -> list[list[int]]:
    rows_a, cols_a = matrix_a.get_size()
    rows_b, cols_b = matrix_b.get_size()

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = Matrix(rows_a, cols_b)

    mul_row = [0] * rows_a
    mul_col = [0] * cols_b

    for i in range(rows_a):
        for j in range(cols_a >> 1):
            mul_row[i] += matrix_a[i][j << 1] * matrix_a[i][(j << 1) + 1]

    for i in range(cols_b):
        for j in range(rows_b >> 1):
            mul_col[i] += matrix_b[j << 1][i] * matrix_b[(j << 1) + 1][i]

    flag = cols_a % 2

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = -mul_row[i] - mul_col[j]

            for k in range(1, cols_a, 2):
                result[i][j] += (matrix_a[i][k - 1] + matrix_b[k][j]) * (matrix_a[i][k] + matrix_b[k - 1][j])

            if flag:
                result[i][j] += matrix_a[i][cols_a - 1] * matrix_b[rows_b - 1][j]

    return result

def multiply_matrixes_strassen(matrix_a, matrix_b):
    rows_a, cols_a = matrix_a.get_size()
    rows_b, cols_b = matrix_b.get_size()

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    size = max(rows_a, cols_a, rows_b, cols_b)
    size = 2 ** (size - 1).bit_length()

    A_padded = [[0] * size for _ in range(size)]
    B_padded = [[0] * size for _ in range(size)]

    for i in range(rows_a):
        for j in range(cols_a):
            A_padded[i][j] = matrix_a[i][j]

    for i in range(rows_b):
        for j in range(cols_b):
            B_padded[i][j] = matrix_b[i][j]

    C_padded = strassen_recursive(A_padded, B_padded)

    C = []
    for i in range(rows_a):
        C.append(C_padded[i][:cols_b])

    return C

def strassen_recursive(matrix_a, matrix_b):
    n = len(matrix_a)

    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]
    
    mid = n // 2
    A11 = [matrix_a[i][:mid] for i in range(mid)]
    A12 = [matrix_a[i][mid:] for i in range(mid)]
    A21 = [matrix_a[i][:mid] for i in range(mid, n)]
    A22 = [matrix_a[i][mid:] for i in range(mid, n)]
    B11 = [matrix_b[i][:mid] for i in range(mid)]
    B12 = [matrix_b[i][mid:] for i in range(mid)]
    B21 = [matrix_b[i][:mid] for i in range(mid, n)]
    B22 = [matrix_b[i][mid:] for i in range(mid, n)]
    
    
    M1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_recursive(matrix_add(A21, A22), B11)
    M3 = strassen_recursive(A11, matrix_sub(B12, B22))
    M4 = strassen_recursive(A22, matrix_sub(B21, B11))
    M5 = strassen_recursive(matrix_add(A11, A12), B22)
    M6 = strassen_recursive(matrix_sub(A11, A21), matrix_add(B11, B12))
    M7 = strassen_recursive(matrix_sub(A12, A22), matrix_add(B21, B22))
    
    
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_sub(matrix_sub(matrix_add(M1, M3), M2), M6)
    
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid, n):
        C.append(C21[i-mid] + C22[i-mid])
    
    return C

def matrix_add(mat_a, mat_b):
    return [[mat_a[i][j] + mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]

def matrix_sub(mat_a, mat_b):
    return [[mat_a[i][j] - mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]

def output_matrix(matrix):
    n = len(matrix); m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()
    print()