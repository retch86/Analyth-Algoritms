void parallel_processing(int n_matr, int m_matr, 
	int cnt_matr, bool matr_is_print, bool compare_time)
{
    std::queue<matrix_t> q1, q2, q3;
    std::mutex m;

    for (int i = 0; i < cnt_matr; i++)  {
        matrix_t matr = generate_matrix(n_matr, m_matr);
        q1.push(matr);

        if (matr_is_print && i == cnt_matr - 1)
        {
            m.lock();
            printf("start matrix:\n");
            print_matrix(matr);
            m.unlock();
        }
    }
    
    bool q1_is_empty = false;
    bool q2_is_empty = false;

    std::vector<matrix_state_t> matrix_state_arr;
    init_matrix_state_arr(matrix_state_arr, cnt_matr);

    std::chrono::time_point<std::chrono::system_clock> time_begin = 
    std::chrono::system_clock::now();

    std::vector<res_time_t> time_result_arr;
    init_time_result_arr(time_result_arr, time_begin, cnt_matr, THREADS_COUNT);

    std::thread threads[THREADS_COUNT];

    threads[0] = std::thread(parallel_stage_1, std::ref(q1), std::ref(q2),
    	std::ref(time_result_arr), std::ref(matrix_state_arr), 
    	std::ref(q1_is_empty));
    threads[1] = std::thread(parallel_stage_2, std::ref(q2), 
    	std::ref(q3), std::ref(time_result_arr), 
    	std::ref(matrix_state_arr), std::ref(q1_is_empty), 
    	std::ref(q2_is_empty));
    threads[2] = std::thread(parallel_stage_3, std::ref(q3), 
    	std::ref(time_result_arr), std::ref(matrix_state_arr), 
    	sstd::ref(q2_is_empty), cnt_matr, matr_is_print);

    for (int i = 0; i < THREADS_COUNT; i++) {
        threads[i].join();
    }

    if (compare_time) {
        printf("     %4d      %s|%s     %4d      %s|%s   %.6f  \n",
            n_matr, PURPLE, BASE_COLOR, 
            cnt_matr, PURPLE, BASE_COLOR,
            time_result_arr[cnt_matr - 1].end);
    }
    else {
        print_res_time(time_result_arr, cnt_matr * THREADS_COUNT);
    }
}
