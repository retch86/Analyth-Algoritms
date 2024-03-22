void stage_1(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q1.front();
    m.unlock();

    matr.min_elem = get_min_elem(matr);

    m.lock();
    q2.push(matr);
    m.unlock();

    m.lock();
    q1.pop();
    m.unlock();
}
