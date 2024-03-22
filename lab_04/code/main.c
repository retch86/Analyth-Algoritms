#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/time.h>

#define LENGTH 10000
#define UPPER_LIM 10000
#define LOWER_LIM  1
#define MAX_LOGICAL_KERNELS 8
#define NSIZE 10
#define NUMITERS 100 


int NUM_THREADS; // число вспомогательных потоков
int NUMBERS_PER_THREAD; // количество элементов массива на поток
int OFFSET; // смещение для последнего потока
int arr[LENGTH];

// Генерация случайных чисел
int generate_random_number(unsigned int lower_limit, unsigned int upper_limit) {
    return rand() % (upper_limit - lower_limit + 1) + lower_limit;
}

// Функция слияния
void merge(int arr[], int left, int middle, int right) {
    int i = 0, j = 0, k = 0;
    int left_length = middle - left + 1;
    int right_length = right - middle;
    int left_array[left_length], right_array[right_length];
    
    // копирование значений левой части массива
    // в вспомогательный 
    for (int i = 0; i < left_length; i ++) {
        left_array[i] = arr[left + i];
    }
    
    // копирование значений правой части массива
    // в вспомогательный 
    for (int j = 0; j < right_length; j ++) {
        right_array[j] = arr[middle + 1 + j];
    }
    
    i = 0;
    j = 0;
    // выбор элементов из вспомогательных
    // массивов для сортировки
    while (i < left_length && j < right_length) {
        if (left_array[i] <= right_array[j]) {
            arr[left + k] = left_array[i];
            i++;
        } else {
            arr[left + k] = right_array[j];
            j++;
        }
        k++;
    }
    
    // копирование оставшихся элементов из вспомогательных
    // массивов в основной
    while (i < left_length) {
        arr[left + k] = left_array[i];
        k++;
        i++;
    }
    while (j < right_length) {
        arr[left + k] = right_array[j];
        k++;
        j++;
    }
}

// Сортировка слиянием
void merge_sort(int arr[], int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;
        merge_sort(arr, left, middle);
        merge_sort(arr, middle + 1, right);
        merge(arr, left, middle, right);
    }
}

// Вывод массива
void output_array(int arr[]) {
    for (int i = 0; i < LENGTH; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Генерация случайного массива
void generate_random_array(int arr[], int length, int lower, int upper) {
    for (int i = 0; i < length; i++) {
        arr[i] = generate_random_number(lower, upper);
    }
}

// Последовательный алгоритм сортировки слиянием
void sequential_merge_sort(int array[], int length) {
    merge_sort(array, 0, length - 1);
}

// Объединение локально отсортированных частей
void merge_sections_of_array(int arr[], int number, int aggregation) {
    for(int i = 0; i < number; i = i + 2) {
        int left = i * (NUMBERS_PER_THREAD * aggregation);
        int right = ((i + 2) * NUMBERS_PER_THREAD * aggregation) - 1;
        int middle = left + (NUMBERS_PER_THREAD * aggregation) - 1;
        if (right >= LENGTH) {
            right = LENGTH - 1;
        }
        merge(arr, left, middle, right);
    }
    if (number / 2 >= 1) {
        merge_sections_of_array(arr, number / 2, aggregation * 2);
    }
}

// Задание каждому потоку для выполнения сортировки слиянием
void *thread_merge_sort(void* arg)
{
    int thread_id = (long)arg;
    int left = thread_id * (NUMBERS_PER_THREAD);
    int right = (thread_id + 1) * (NUMBERS_PER_THREAD) - 1;
    if (thread_id == NUM_THREADS - 1) {
        right += OFFSET;
    }
    int middle = left + (right - left) / 2;
    if (left < right) {
        merge_sort(arr, left, right);
        merge_sort(arr, left + 1, right);
        merge(arr, left, middle, right);
    }
    return NULL;
}

// Параллельный алгоритм сортировки слиянием
void __parallel_merge_sort() {
    pthread_t threads[NUM_THREADS];
    
    for (long i = 0; i < NUM_THREADS; i ++) {
        int rc = pthread_create(&threads[i], NULL, thread_merge_sort, (void *)i);
        if (rc){
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            exit(-1);
        }
    }
    
    for(long i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    merge_sections_of_array(arr, NUM_THREADS, 1);
}

void parallel_merge_sort() {
    NUM_THREADS = MAX_LOGICAL_KERNELS / 2;
    OFFSET = LENGTH % NUM_THREADS;
    NUMBERS_PER_THREAD = LENGTH / NUM_THREADS;

    __parallel_merge_sort();
}

// Результаты расчета последовательной реализации от длины массива
void stat_time_input_size() {
    struct timeval  start, end;
    double time_spent;
    FILE *file_seq, *file_parallel;

    int array[LENGTH];
    double time_array[NSIZE];
    int sizes[NSIZE] = {1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000};

    generate_random_array(array, LENGTH, LOWER_LIM, UPPER_LIM);
    
    for (int size = 1000, i = 0; size <= 10000; size += 1000, i++){
        for (int k = 0; k < NUMITERS; k++) {
            gettimeofday(&start, NULL);
            sequential_merge_sort(array, size);
            gettimeofday(&end, NULL);

            time_spent = ((double) ((double) (end.tv_usec - start.tv_usec) / 1000000 +
                                (double) (end.tv_sec - start.tv_sec)));
            time_array[i] += time_spent;
        }
    }

    file_seq = fopen("time_input_size.txt", "w");
    fprintf(file_seq, "size time_spent\n");
    for (int i = 0; i < NSIZE; i++) {
        time_array[i] /= NUMITERS;
        fprintf(file_seq, "%d %f\n", sizes[i], time_array[i]);
    }

    fclose(file_seq);
}

// Результаты расчета последовательной реализации и
// с 1 вспомогательным потоком
void stat_time_1_add_thread() {
    struct timeval  start, end;
    double time_spent;
    FILE *file_parallel;
    double time_array[NSIZE];
    int sizes[NSIZE] = {1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000};

    
    NUM_THREADS = 1;
    
    for (int size = 1000, i = 0; size <= 10000; size += 1000, i++){
        for (int k = 0; k < NUMITERS; k++) {
            OFFSET = size % NUM_THREADS;
            NUMBERS_PER_THREAD = size / NUM_THREADS;
            generate_random_array(arr, size, LOWER_LIM, UPPER_LIM);
            gettimeofday(&start, NULL);
            parallel_merge_sort();
            gettimeofday(&end, NULL);

            time_spent = ((double) ((double) (end.tv_usec - start.tv_usec) / 1000000 +
                                (double) (end.tv_sec - start.tv_sec)));
            

            time_array[i] += time_spent;
        }
    }

    file_parallel = fopen("time_1_add_thread.txt", "w");
    fprintf(file_parallel, "size time_spent\n");
    for (int i = 0; i < NSIZE; i++) {
        time_array[i] /= NUMITERS;
        fprintf(file_parallel, "%d %f\n", sizes[i], time_array[i]);
    }
    fclose(file_parallel);
}

// Результаты расчета параллельной реализации от числа потоков
void stat_time_n_kernels() {
    struct timeval  start, end;
    double time_spent;
    FILE *file_parallel;
    double time_array[NSIZE];

    
    int max_threads = 8 * MAX_LOGICAL_KERNELS, size = 1000;
    for (int num_threads = 1, i = 0; num_threads <= max_threads; num_threads *= 2, i++){
        for (int k = 0; k < NUMITERS; k++) {
            NUM_THREADS = num_threads;
            OFFSET = size % NUM_THREADS;
            NUMBERS_PER_THREAD = size / NUM_THREADS;

            generate_random_array(arr, size, LOWER_LIM, UPPER_LIM);

            gettimeofday(&start, NULL);
            parallel_merge_sort();
            gettimeofday(&end, NULL);

            time_spent = ((double) ((double) (end.tv_usec - start.tv_usec) / 1000000 +
                                (double) (end.tv_sec - start.tv_sec)));
            time_array[i] += time_spent;
        }
    }

    file_parallel = fopen("time_n_kernels.txt", "w");
    fprintf(file_parallel, "n_kernels time_spent\n");
    for (int num_threads = 1, i = 0; num_threads <= max_threads; num_threads *= 2, i++) {
        time_array[i] /= NUMITERS;
        fprintf(file_parallel, "%d %f\n", num_threads, time_array[i]);
    }
    fclose(file_parallel);
}

void statistics() {
    stat_time_1_add_thread();
    stat_time_input_size();
    stat_time_n_kernels();  
}

int main(int argc, const char * argv[]) {
    srand(time(NULL));

    int array[LENGTH];
    generate_random_array(array, LENGTH, LOWER_LIM, UPPER_LIM);
    sequential_merge_sort(array, LENGTH);

    parallel_merge_sort();
    
    statistics();
    return 0;
}