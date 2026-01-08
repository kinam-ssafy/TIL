/*
boj1463 - 1로 만들기

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

dp[i] = 정수 i를 만드는 연산 최솟값?

X = 1, 1
X = 2, 1
X = 3, 1
X = 4, 2
X = 5, 5 - 1 = 4, 4 - 1 = 3, 3 /  3 = 1, 3
X = 6, 2
X = 7, 3
X = 8, 3
X = 9, 2
X = 10, 3

dp[10] 은 어떻게 구하지?
경우가 3가지를 거꾸로 생각하면 1을 더한다, 2 곱한다 3곱한다
dp[9]에서 1을 더함 = dp[9] + 1
dp[5]에서 2를 곱합 = dp[5] + 1
dp[10/3]에서 3을 곱합 = dp[10/3] + 1 << 없으니까 조건 걸어주기

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    for (int i = 4; i <= n; i++) {
        if (i % 3 == 0 && i % 2 == 0) {
            dp[i] = min({dp[i - 1] + 1, dp[i / 2] + 1, dp[i / 3] + 1});
        }
        else if (i % 3 == 0) {
            dp[i] = min(dp[i - 1] + 1, dp[i / 3] + 1);
        }
        else if (i % 2 == 0) {
            dp[i] = min(dp[i - 1] + 1, dp[i / 2] + 1);
        }
        else {
            dp[i] = dp[i - 1] + 1;
        }
        
    }

    cout << dp[n];

    return 0;
}