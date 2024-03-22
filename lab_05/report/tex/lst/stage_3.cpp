void stage_3(std::queue<matrix_t> &q3, int task_num, int cnt_matr, bool matr_is_print)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q3.front();
    m.unlock();

    matr.sum_elem = get_sum_elements(matr);
    
    if (matr_is_print && task_num == cnt_matr)
    {
        printf("\nmin_elem = %d\n\nmatrix after 2 step:\n", matr.min_elem);
        print_matrix(matr);
        printf("\nsum_elem = %d\n\n", matr.sum_elem);
    }

    m.lock();
    q3.pop();
    m.unlock();
}
