def multiply_matrixes_strassen(matrix_a, matrix_b):
    rows_a, cols_a = matrix_a.get_size()
    rows_b, cols_b = matrix_b.get_size()

    if cols_a != rows_b:
        return "Умножение невозможно"

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
