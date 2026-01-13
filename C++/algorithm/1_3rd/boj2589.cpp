/* boj2589 - 보물섬 

보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.



예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.



보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.


첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.
*/

#include <iostream>
#include <deque>
#include <string>

using namespace std;

int N, M;
char arr[50][50]; // 보물 지도의 크기는 50, 50 이하 

// 3개의 값 묶어서 넣기 위한 tuple같은거 선언
struct Node {
    int i;
    int j;
    int dist;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);  

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        string s;
        cin >> s; // "LWWLWLW" 이런식으로 한 줄의 string을 입력받을 것

        for (int j = 0; j < M; j++) {
            arr[i][j] = s[j];
        }
    }

    int di[4] = {0, 1, 0, -1};
    int dj[4] = {1, 0, -1, 0};

    int ans = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (arr[i][j] == 'L') {
                // 매 BFS마다 방문배열 초기화
                int visited[50][50] = {0};
                deque<Node> q;
                q.push_back({i, j, 0});
                visited[i][j] = 1;

                while (!q.empty()) {
                    Node current = q.front();
                    int ci = current.i;
                    int cj = current.j;
                    int dist = current.dist;
                    q.pop_front();

                    if (ans < dist) {
                        ans = dist;
                    }
                    
                    for (int d = 0; d < 4; d++) {
                        int ni, nj;
                        ni = ci + di[d];
                        nj = cj + dj[d];

                        //python식 조건문 쓰지않기위해 박제
                        //if ((0 <= ni < N) and (0 <= nj < M) and (visited[ni][nj] == 0) and (arr[ni][nj] == 'L')) 
                        if (0 <= ni && ni < N && 0 <= nj && nj < M && visited[ni][nj] == 0 && arr[ni][nj] == 'L') {
                            visited[ni][nj] = 1;
                            q.push_back({ni, nj, dist + 1});
                        }
                    }
                }
            }
        }
    }
    cout << ans;



    return 0;
}