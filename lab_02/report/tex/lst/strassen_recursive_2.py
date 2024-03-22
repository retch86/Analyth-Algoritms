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
