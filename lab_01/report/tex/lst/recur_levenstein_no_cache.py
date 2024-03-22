def recursive_levenstein(str_1: str, str_2: str) -> int:
    if str_1 == '' or str_2 == '':
        return abs(len(str_1) - len(str_2))
    match = 0 if str_1[-1] == str_2[-1] else 1
    distance = min(recursive_levenstein(str_1, str_2[:-1]) + 1,
                   recursive_levenstein(str_1[:-1], str_2) + 1,
                   recursive_levenstein(str_1[:-1], str_2[:-1]) + match)
    return distance
