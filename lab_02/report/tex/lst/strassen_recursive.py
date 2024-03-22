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
