def recursive_levenstein_matrix(str_1: str, str_2: str, 
	i: int, j: int, matrix: list[list[int]]) \
                                -> Tuple[int, list[list[int]]]:
    if i == 0:
        return j, matrix
    if j == 0:
        return i, matrix
    if matrix[i][j] != -1:
        return matrix[i][j], matrix
    match = 0 if str_1[-1] == str_2[-1] else 1

    insert, matrix = recursive_levenstein_matrix(
    					str_1, str_2[:-1], i, j - 1, matrix)
    delete, matrix = recursive_levenstein_matrix(
    					str_1[:-1], str_2, i - 1, j, matrix)
    replace, matrix = recursive_levenstein_matrix(
    					str_1[:-1], str_2[:-1], i - 1, j - 1, matrix)
    insert += 1; delete += 1; replace += match

    distance = min(insert, delete, replace)
    matrix[i][j] = distance
    return distance, matrix
