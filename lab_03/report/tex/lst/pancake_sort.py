def pancake_sort(arr, n):
    while n > 1:
        max_i = max_index(arr, n)
        if max_i != n - 1:
            if max_i != 0:
                flip(arr, max_i)
            flip(arr, n - 1)
        n -= 1
