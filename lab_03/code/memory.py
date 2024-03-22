import cProfile, pstats, sys
from numbers_array import form_random_array
from sorts import pancake_sort, select_sort, quick_sort

def get_memory_usage():
    for num in range(100, 201, 100):
        array = form_random_array(num)
        size = num
        cProfile.run(f"pancake_sort({array}, {size})", f"memory_pancake_{num}.dat")
        with open (f"memory_pancake_{num}.txt", "w") as file:
            p = pstats.Stats(f"memory_pancake_{num}.dat", stream=file)
            p.sort_stats("calls").print_stats()
        print(f"size_pancake_{num} = {sys.getsizeof(pancake_sort)}")

        cProfile.run(f"quick_sort({array}, {0}, {size-1})", f"memory_quick_{num}.dat")
        with open (f"memory_quick_{num}.txt", "w") as file:
            p = pstats.Stats(f"memory_quick_{num}.dat", stream=file)
            p.sort_stats("calls").print_stats()
        print(f"size_quick_{num} = {sys.getsizeof(quick_sort)}")

        cProfile.run(f"select_sort({array}, {size})", f"memory_select_{num}.dat")
        with open (f"memory_select_{num}.txt", "w") as file:
            p = pstats.Stats(f"memory_select_{num}.dat", stream=file)
            p.sort_stats("calls").print_stats()
        print(f"size_select_{num} = {sys.getsizeof(select_sort)}")