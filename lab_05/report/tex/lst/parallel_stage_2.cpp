void parallel_stage_2(std::queue<matrix_t> &q2, std::queue<matrix_t> &q3,
                      std::vector<res_time_t> &time_result_arr,
                      std::vector<matrix_state_t> &matrix_state_arr, 
                      bool &q1_is_empty, bool &q2_is_empty)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    int task_num = 1;
    while(true) {      
        if (!q2.empty()) {   
            if (matrix_state_arr[task_num - 1].stage_1 == true) {
                time_start = std::chrono::system_clock::now();
                stage_2(std::ref(q2), std::ref(q3));
                time_end = std::chrono::system_clock::now();

                save_result(time_result_arr, time_start, time_end,
                	 time_result_arr[0].time_begin, task_num, 2);

                matrix_state_arr[task_num - 1].stage_2 = true;
                task_num++;
            }
        }
        else if(q1_is_empty) {
            break;
        }
    }
    q2_is_empty = true;
}
