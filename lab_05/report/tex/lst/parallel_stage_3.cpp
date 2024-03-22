void parallel_stage_3(std::queue<matrix_t> &q3, 
                      std::vector<res_time_t> &time_result_arr,
                      std::vector<matrix_state_t> &matrix_state_arr, 
                      bool &q2_is_empty, int cnt_matr, bool matr_is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    int task_num = 1;

    while(true)
    {      
        if (!q3.empty())
        {   
            if (matrix_state_arr[task_num - 1].stage_2 == true)
            {
                time_start = std::chrono::system_clock::now();
                stage_3(std::ref(q3), task_num, cnt_matr, matr_is_print);
                time_end = std::chrono::system_clock::now();

                save_result(time_result_arr, time_start, time_end,
                	 time_result_arr[0].time_begin, task_num, 3);

                matrix_state_arr[task_num - 1].stage_3 = true;
                task_num++;
            }
        }
        else if(q2_is_empty)
        {
            break;
        } 
    }
}
