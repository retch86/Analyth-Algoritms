#@profile
def flip(arr, k: int):
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        k -= 1
        left += 1
#@profile
def max_index(arr, k: int) -> int:
    index = 0
    for i in range(k):
        if arr[i] > arr[index]:
            index = i
    return index

#@profile
def pancake_sort(arr, n):
    while n > 1:
        max_i = max_index(arr, n)
        if max_i != n - 1:
            if max_i != 0:
                flip(arr, max_i)
            flip(arr, n - 1)
        n -= 1
#@profile
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
 
    return i + 1
 
#@profile 
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
 
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

#@profile
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
