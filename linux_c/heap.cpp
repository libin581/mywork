//https://www.thinksaas.cn/group/topic/597782/
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

template <class T>
struct display
{
    void operator()(const T &x)
    {
        cout << x << " ";
    }
};

/// heapĬ��Ϊ��ѣ���������Ϊ����С��
template <typename T>
struct greator
{
    bool operator()(const T &x, const T &y)
    {
        return x > y;
    }
};

int main(void)
{
    int ia[9] = { 0, 1, 2, 3, 4, 8, 9, 3, 5 };
    vector<int> ivec(ia, ia + 9);

    make_heap(ivec.begin(), ivec.end(), greator<int>()); //ע�⣺�˺�������ʱ����Ԫ��Ӧ��ֹ�ڵײ�������β��
    for_each(ivec.begin(), ivec.end(), display<int>());
    cout << endl;

    ivec.push_back(7);
    push_heap(ivec.begin(), ivec.end(), greator<int>());
    for_each(ivec.begin(), ivec.end(), display<int>());
    cout << endl;

    pop_heap(ivec.begin(), ivec.end(), greator<int>());
    cout << ivec.back() << endl;
    ivec.pop_back();
    for_each(ivec.begin(), ivec.end(), display<int>());
    cout << endl;

    sort_heap(ivec.begin(), ivec.end(), greator<int>());
    for_each(ivec.begin(), ivec.end(), display<int>());
    cout << endl;

    return 0;
}