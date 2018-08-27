#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main(void)
{
    int ia[9] = { 0, 1, 2, 3, 4, 8, 9, 3, 5 };
    vector<int> ivec(ia, ia + 9);

    priority_queue<int> ipq(ivec.begin(), ivec.end());

    ipq.push(7);
    ipq.push(23);
    while (!ipq.empty())
    {
        cout << ipq.top() << " ";
        ipq.pop();
    }
    cout << endl;

    return 0;
}