from time import process_time
from numbers_array import *
from sorts import *

def timing_order_array(count_repeats: int, form_array):
    pancake_time = list()
    quick_time = list()
    select_time = list()

    for size in range(100, 991, 100):
        average_time_pancake = 0
        average_time_quick = 0
        average_time_select = 0
        if size % 100 == 0:
            print(f"{size / 10} %")
        for j in range(count_repeats):
            order_array = form_array(size)
            time_start = process_time()
            pancake_sort(order_array, size)
            time_end = process_time()
            average_time_pancake += time_end - time_start

            order_array = form_array(size)
            time_start = process_time()
            quick_sort(order_array, 0, size-1)
            time_end = process_time()
            average_time_quick += time_end - time_start

            order_array = form_array(size)
            time_start = process_time()
            select_sort(order_array, size)
            time_end = process_time()
            average_time_select += time_end - time_start
        average_time_pancake /= count_repeats
        average_time_quick /= count_repeats
        average_time_select /= count_repeats
        pancake_time.append(average_time_pancake)
        quick_time.append(average_time_quick)
        select_time.append(average_time_select)

    return pancake_time, quick_time, select_time