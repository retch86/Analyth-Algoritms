def max_index(arr, k: int) -> int:
    index = 0
    for i in range(k):
        if arr[i] > arr[index]:
            index = i
    return index
