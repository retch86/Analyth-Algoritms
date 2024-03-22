void linear_processing(int n_matr, int m_matr, int cnt_matr, bool matr_is_print, bool compare_time)
{
    std::queue<matrix_t> q1, q2, q3;
    std::mutex m;

    for (int i = 0; i < cnt_matr; i++) {
        matrix_t matr = generate_matrix(n_matr, m_matr);
        q1.push(matr);

        if (matr_is_print && i == cnt_matr - 1) {
            m.lock();
            printf("start matrix:\n");
            print_matrix(matr);
            m.unlock();
        }
    }

    std::vector<matrix_state_t> matrix_state_arr;
    init_matrix_state_arr(matrix_state_arr, cnt_matr);

    std::chrono::time_point<std::chrono::system_clock> time_start, time_end, 
    time_begin = std::chrono::system_clock::now();

    std::vector<res_time_t> time_result_arr;
    init_time_result_arr(time_result_arr, time_begin, cnt_matr, THREADS_COUNT);

    for (int i = 0; i < cnt_matr; i++)
    {
        time_start = std::chrono::system_clock::now();
        stage_1(std::ref(q1), std::ref(q2));
        time_end = std::chrono::system_clock::now();
        
        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 1);

        time_start = std::chrono::system_clock::now();
        stage_2(std::ref(q2), std::ref(q3));
        time_end = std::chrono::system_clock::now();

        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 2);

        time_start = std::chrono::system_clock::now();
        stage_3(std::ref(q3), i + 1, cnt_matr, matr_is_print);
        time_end = std::chrono::system_clock::now();

        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 3);
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
