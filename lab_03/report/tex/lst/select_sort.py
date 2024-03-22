def select_sort(array, n):
    if n == 0:
        print("Ошибка")
        return array
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
    return array

