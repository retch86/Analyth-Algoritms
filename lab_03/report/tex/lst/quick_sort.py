def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
 
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
