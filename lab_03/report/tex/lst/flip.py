def flip(arr, k: int):
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        k -= 1
        left += 1
