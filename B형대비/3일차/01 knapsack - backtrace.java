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
            come = new int[N + 1][K + 1];
                // come[i][j] := 1 ; i번 물건을 안 쓰는 게 더 좋았다.
                // come[i][j] := 2 ; i번 물건을 쓰는 게 더 좋았다.
            w = new int[101];
            v = new int[101];
            ans = 0;

            for (int i = 1; i <= N; i++) {
                int size = scann.nextInt();
                int value = scann.nextInt();
                w[i] = size;
                v[i] = value;
            }

            for (int i = 1; i <= N; i++) {
                for (int j = 0; j <= K; j++) {
                    // 1번째 선택
                    dp[i][j] = dp[i - 1][j];
                    come[i][j] = 1;

                    if (w[i] <= j) {
                        // 만약 2번째 선택이 더 좋다?
                        if (dp[i][j] < dp[i - 1][j - w[i]] + v[i]) {
                            dp[i][j] = dp[i - 1][j - w[i]] + v[i];
                            come[i][j] = 2;
                        }
                        
                    }
                }
            }

            int[] used = new int[N + 1];  // used[i] := i번 물건이 사용되었는가?
            int j = K;  // 현재 가방 용량
            
            for (int i = N; i >= 1; i--) {
                // 현재 j 만큼의 용량을 쓴 상태
                if (come[i][j] == 1) {
                    // i 번 물건을 안 쓰는 게 더 좋았다.
                    used[i] = 0;
                }else {
                    // i 번 물건을 쓰는 게 더 좋았다.
                    used[i] = 1;
                    j -= w[i];
                }
            }

            for (int i= 1;i<=N;i++){
                System.out.println(i + "번 물건 사용: " + used[i]);
            }


            System.out.println("#" + testcase + " " + dp[N][K]);
        }
    }
}