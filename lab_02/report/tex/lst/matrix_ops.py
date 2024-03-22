def matrix_add(mat_a, mat_b):
    return [[mat_a[i][j] + mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]

def matrix_sub(mat_a, mat_b):
    return [[mat_a[i][j] - mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]
