def recursive_dameray_levenstein(str_1: str, str_2: str) -> int:
    if str_1 == '' or str_2 == '':
        return abs(len(str_1) - len(str_2))
    match = 0 if str_1[-1] == str_2[-1] else 1
    insert = recursive_dameray_levenstein(str_1, str_2[:-1]) + 1
    delete = recursive_dameray_levenstein(str_1[:-1], str_2) + 1
    replace = recursive_dameray_levenstein(str_1[:-1], str_2[:-1]) + match
    if len(str_1) > 1 and len(str_2) > 1 and str_1[-1] == str_2[-2] and \
    str_2[-1] == str_1[-2]:
        distance = min(insert, delete, replace, 
        	recursive_dameray_levenstein(str_1[:-2], str_2[:-2]) + 1)
    else:
        distance = min(insert, delete, replace)
    return distance
