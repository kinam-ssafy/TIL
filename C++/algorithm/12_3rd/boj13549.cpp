/* boj13549 - 숨바꼭질 3
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

*/

// BFS

#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    int N, K;
    cin >> N >> K;
    int INF = 1000000;
    vector<int> visited(100001, INF);
    deque<int> dq;

    // 시작 위치
    visited[N] = 0;
    dq.push_back(N);

    while (!dq.empty()) {
        int current = dq.front();
        dq.pop_front(); // 반환이 안됨

        // 종료 조건
        if (current == K) {
            cout << visited[K];
            return 0;
        }

        // 순간이동
        int teleport = current * 2;
        // 범위 조건 + 더 작으면 갱신
        if (teleport <= 100000 && visited[teleport] > visited[current]) {
            visited[teleport] = visited[current];
            dq.push_front(teleport);
        }

        // +1로 걷기
        int plus = current + 1;
        int next = visited[current] + 1;
        if (plus <= 100000 && next < visited[plus]) {
            visited[plus] = next; // 1초 걸림
            dq.push_back(plus);
        }
        // -1로 걷기
        int minus = current - 1;
        if (0 <= minus && minus <= 100000 && next < visited[minus]) {
            visited[minus] = next; // 1초 걸림
            dq.push_back(minus);
        }
    }


    return 0;
}