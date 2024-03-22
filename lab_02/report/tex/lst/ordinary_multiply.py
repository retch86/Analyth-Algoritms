def multiply_matrixes_ordinary(matrix_a, matrix_b) -> list[list[int]]:
    n, m = matrix_a.get_size(); q, p = matrix_b.get_size()
    if m != q:
        print('Несовпадение размеров матриц')
        return
    else:
        matrix_result = Matrix(n, p)
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    matrix_result[i][j] = 
                    	matrix_result[i][j] + matrix_a[i][k] * matrix_b[k][j]
        return matrix_result
