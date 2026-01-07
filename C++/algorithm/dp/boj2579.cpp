/*
boj2579: 계단 오르기
계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 
<그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.

연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

dp[i]는 i번째 계단 올라갔을 때 최댓값
dp[i]가 되는 경우의 수?
i-1번 계단을 밟고 오는경우
    >> i-2번 계단은 못밟음. 그럼 얘는 i-3번을 밟아야함
i-2번 계단을 밟고 i-1은 건너뛰고온경우
    >> 얘는 i-3번 밟았을수도있고 i-4번 밟았을수도있음

dp[i] = stairs[i] + max(dp[i - 3] + stairs[i - 1], dp[i - 2])


*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> stairs(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> stairs[i];
    }
    
    vector<int> dp(n + 1);
    dp[0] = 0;
    dp[1] = stairs[1];
    dp[2] = dp[1] + stairs[2];
    for (int i = 3; i <= n; i++) {
        dp[i] = stairs[i] + max(dp[i - 3] + stairs[i - 1], dp[i - 2]);
    }

    cout << dp[n];

    return 0;
}