from constants import *
from numbers_array import *
from sorts import *
from test_time import *
from graph import *
from menu import *
import sys
from memory import get_memory_usage

def main():
    choice = -1
    while choice != 0:
        menu()
        choice = int(input("Выберите пункт меню: "))
        if choice == 0:
            sys.exit()
        elif choice == 1:
            print('Исходный массив')
            array = form_random_array(MAX_SIZE_ARRAY)
            size = len(array)
            output_array(array, size)
            pancake_sort(array, size)
            print('Отсортированный массив')
            output_array(array, size)
        elif choice == 2:
            print('Исходный массив')
            array = form_random_array(MAX_SIZE_ARRAY)
            size = len(array)
            output_array(array, size)
            quick_sort(array, 0, size-1)
            print('Отсортированный массив')
            output_array(array, size)
        elif choice == 3:
            print('Исходный массив')
            array = form_random_array(MAX_SIZE_ARRAY)
            size = len(array)
            output_array(array, size)
            select_sort(array, size)
            print('Отсортированный массив')
            output_array(array, size)
        elif choice == 4:
            output_graph()
        elif choice == 5:
            get_memory_usage()
if __name__ == "__main__":
    main()