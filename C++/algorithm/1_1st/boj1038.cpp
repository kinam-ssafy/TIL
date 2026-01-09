/*
boj1038 - 감소하는 수

음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. 
N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 
0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 
만약 N번째 감소하는 수가 없다면 -1을 출력한다.

0, 0번째 감소하는 수
1~9, 1~9번째 감소하는 수
10, 10번째
11, x
12
20, 11번째 
21, 12번째 감소하는수
30, 13
31, 14
32, 15

규칙?
동일한 수는 못 들어감
중복 x 뽑기
감소하는 수 모두 만들기

숫자로 백트래킹 BFS 수행?

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> ans; // 크기 지정 x
    queue<long long> q;

    // 0~9까지는 일단 집어넣기
    for (int i = 0; i < 10; i++) {
        ans.push_back(i);
        q.push(i);
    }

    while (!q.empty()) { 
        long long current = q.front(); // 맨 앞 반환
        q.pop(); // 맨 앞 제거
        // 파이썬이면 popleft()면 됐을텐데 C++은 반환, 제거 따로
        int last = current % 10; // 마지막 숫자

        for (int i = 0; i < last; i++) {
            long long next = current * 10 + i;

            q.push(next);
            ans.push_back(next);
        }
    }

    sort(ans.begin(), ans.end());

    if (n >= ans.size()) {
        cout << -1;
    }
    else {
        cout << ans[n];
    }

    return 0;
}