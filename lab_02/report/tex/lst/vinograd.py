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
                mul_u[i] = mul_u[i] + 
                	matrix_a[i][2*j] * matrix_a[i][2*j + 1]

        mul_w = [0] * p
        for i in range(p):
            for j in range(d):
                mul_w[i] = mul_w[i] + 
                	matrix_b[2*j][i] * matrix_b[2*j + 1][i]

        for i in range(n):
            for j in range(p):
                matrix_result[i][j] = -mul_u[i] - mul_w[j]
                for k in range(d):
                    matrix_result[i][j] = 
                    	matrix_result[i][j] + 
                    		(matrix_a[i][2*k] + matrix_b[2*k+1][j]) * \
                                (matrix_a[i][2*k+1] + matrix_b[2*k][j])
                                                    
        if m % 2 == 1:
            for i in range(n):
                for j in range(p):
                    matrix_result[i][j] = matrix_result[i][j] + 
                    	matrix_a[i][m-1] * matrix_b[m-1][j]

        return matrix_result
