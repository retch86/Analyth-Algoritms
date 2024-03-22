import matplotlib.pyplot as plt
from test_time import *

def output_graph() -> None:
    print('Лучший случай')
    best_pancake_time, best_quick_time, best_select_time = timing_order_array(COUNT_ITERATIONS, form_order_array)
    print('Обычный случай')
    usual_pancake_time, usual_quick_time, usual_select_time = timing_order_array(COUNT_ITERATIONS, form_random_array)
    print('Худший случай')
    worst_pancake_time, worst_quick_time, worst_select_time = timing_order_array(COUNT_ITERATIONS, form_reverse_order_array)
    print(best_quick_time)
    write_to_file('best_pancake_time.txt', best_pancake_time)
    write_to_file('best_quick_time.txt', best_quick_time)
    write_to_file('best_select_time.txt', best_select_time)
    write_to_file('usual_pancake_time.txt', usual_pancake_time)
    write_to_file('usual_quick_time.txt', usual_quick_time)
    write_to_file('usual_select_time.txt', usual_select_time)
    write_to_file('worst_pancake_time.txt', worst_pancake_time)
    write_to_file('worst_quick_time.txt', worst_quick_time)
    write_to_file('worst_select_time.txt', worst_select_time)

    create_graph(best_pancake_time, best_quick_time, best_select_time, 'Лучший случай')
    create_graph(usual_pancake_time, usual_quick_time, worst_select_time, 'Обычный случай')
    create_graph(worst_pancake_time, worst_quick_time, usual_select_time, 'Худший случай')

def write_to_file(string, array):
    with open(string, 'w') as file:
        for i in range(len(array)):
            file.write(str((i+1) * 100) + ' ' + str(array[i]) + '\n')


def create_graph(pancake_time:list[int], quick_time:list[int],
                select_time:list[int], title:str):
    ax = plt.subplot(121)
    len_array = [100, 200, 300, 400, 500, 600, 700, 800, 900]

    plt.title(title)
    ax.plot(len_array, pancake_time, label="Блинная", marker='o')
    ax.plot(len_array, quick_time, label="Быстрая", marker='o')
    ax.plot(len_array, select_time, label="Выбором", marker='o')

    plt.legend(loc=2, bbox_to_anchor=(1, 0.5))
    ax.grid()
    ax.set_xlabel('Число элементов')
    ax.set_ylabel('Время (с)')
    ax.set_xlim([0, 1050])

    plt.show()