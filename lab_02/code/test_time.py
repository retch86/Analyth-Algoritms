from time import process_time
from matrix import *

def measure_time():
    print("Лучший случай:")
    best_ordinary, best_vinograd, best_optimized_vinograd, best_strassen = measure_process_time(100, 1001, 100)
    with open('best_ordinary.txt', 'w') as file:
        for listitem in best_ordinary:
            file.write(str(listitem) + '\n')

    with open('best_vinograd.txt', 'w') as filehandle:  
        for listitem in best_vinograd:
            filehandle.write(str(listitem) + '\n')

    with open('best_optimized_vinograd.txt', 'w') as filehandle:  
        for listitem in best_optimized_vinograd:
            filehandle.write(str(listitem) + '\n')

    with open('best_strassen.txt', 'w') as filehandle:  
        for listitem in best_strassen:
            filehandle.write(str(listitem) + '\n')
    print("Худший случай:")
    worst_ordinary, worst_vinograd, worst_optimized_vinograd, worst_strassen = measure_process_time(101, 1002, 100)

    with open('worst_ordinary.txt', 'w') as filehandle:  
        for listitem in worst_ordinary:
            filehandle.write(str(listitem) + '\n')

    with open('worst_vinograd.txt', 'w') as filehandle:  
        for listitem in worst_vinograd:
            filehandle.write(str(listitem) + '\n')

    with open('file_6.txt', 'w') as filehandle:  
        for listitem in worst_optimized_vinograd:
            filehandle.write(str(listitem) + '\n')

    with open('worst_strassen.txt', 'w') as file:
        for listitem in worst_strassen:
            file.write(str(listitem) + '\n')

def measure_process_time(start, end, step):
    ordinary= []; vinograd = []; optimized_vinograd = []; strassen=[]
    
    for i in range(start, end, step):
        matrix_a = Matrix(i, i)
        matrix_b = Matrix(i, i)
        avg_time_ordinary = 0
        avg_time_vinograd = 0
        avg_time_optimized_vinograd = 0
        avg_time_strassen = 0

        for count in range(1,2):
            
            time_start = process_time()
            multiply_matrixes_ordinary(matrix_a, matrix_b)
            time_end = process_time()
            avg_time_ordinary += time_end - time_start

            time_start = process_time()
            multiply_matrixes_vinograd(matrix_a, matrix_b)
            time_end = process_time()
            avg_time_vinograd += time_end - time_start

            time_start = process_time()
            multiply_matrixes_vinograd_optimized(matrix_a, matrix_b)
            time_end = process_time()
            avg_time_optimized_vinograd += time_end - time_start

            time_start = process_time()
            multiply_matrixes_strassen(matrix_a, matrix_b)
            time_end = process_time()
            avg_time_strassen += time_end - time_start
            
        ordinary.append(avg_time_ordinary/count)
        vinograd.append(avg_time_vinograd/count)
        optimized_vinograd.append(avg_time_optimized_vinograd/count)
        strassen.append(avg_time_strassen/count)
        if start == 101 and (i - 1) % 100 == 0:
            print(f"{i / 10} %")
        elif start == 100 and i % 100 == 0:
            print(f"{i / 10} %") 
    return ordinary, vinograd, optimized_vinograd, strassen