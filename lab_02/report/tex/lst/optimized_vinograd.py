def multiply_matrixes_vinograd_optimized(matrix_a, matrix_b) -> list[list[int]]:
    rows_a, cols_a = matrix_a.get_size()
    rows_b, cols_b = matrix_b.get_size()

    if cols_a != rows_b:
        return "Умножение невозможно."

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
                result[i][j] += 
                	(matrix_a[i][k - 1] + matrix_b[k][j]) * 
                		(matrix_a[i][k] + matrix_b[k - 1][j])

            if flag:
                result[i][j] += 
                	matrix_a[i][cols_a - 1] * matrix_b[rows_b - 1][j]

    return result
