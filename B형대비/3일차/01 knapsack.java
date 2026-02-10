import java.util.Scanner;

public class Solution {
    static int N;
    static int K;
    static int dp[][], come[][], w[], v[];
    static int ans;

    public static void main(String[] args) {
        Scanner scann = new Scanner(System.in);
        int T = scann.nextInt();
        for (int testcase = 1; testcase <= T; testcase++) {
            N = scann.nextInt();
            K = scann.nextInt();
            dp = new int[N + 1][K + 1];
            w = new int[101];
            v = new int[101];
            ans = 0;

            for (int i = 1; i <= N; i++) {
                int size = scann.nextInt();
                int value = scann.nextInt();
                w[i] = size;
                v[i] = value;
            }

            for (int i = 1; i <= N; i++) {          // i 개의 물건을 사용할 수 있따.
                for (int j = 0; j <= K; j++) {      // j 부피의 가방이다
                    // 1번째 선택
                    dp[i][j] = dp[i - 1][j];

                    if (w[i] <= j) {  // 애초에 i 번 물건을 가방에 못 넣는 경우를 제외하자.
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
                    }
                }
            }

            System.out.println("#" + testcase + " " + dp[N][K]);
        }
    }
}