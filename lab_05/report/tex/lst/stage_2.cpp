void stage_2(std::queue<matrix_t> &q2, std::queue<matrix_t> &q3)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q2.front();
    m.unlock();

    mod_by_min_elem(matr);
    
    m.lock();
    q3.push(matr);
    m.unlock();
    
    m.lock();
    q2.pop();
    m.unlock();
}
