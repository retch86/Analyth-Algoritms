void parallel_merge_sort() {
    struct timeval  start, end;
    double time_spent;

    pthread_t threads[NUM_THREADS];

	// Назначение каждому потоку задание -- сортировка
    for (long i = 0; i < NUM_THREADS; i ++) {
        int rc = pthread_create(&threads[i], NULL, 
        	thread_merge_sort, (void *)i);
        if (rc){
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            exit(-1);
        }
    }
    
    // Ожидание завершения всех потоков
    for(long i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
	
	// Слияние результатов потоков
    merge_sections_of_array(arr, NUM_THREADS, 1);
}
