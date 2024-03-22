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
    
    i = 0, j = 0;
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
