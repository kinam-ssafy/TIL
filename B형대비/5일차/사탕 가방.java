import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int N = Integer.parseInt(st.nextToken());
            long M = Long.parseLong(st.nextToken());
            st = new StringTokenizer(br.readLine(), " ");
            Long[] candy = new Long[N];
            long max = Long.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                candy[i] = Long.valueOf(st.nextToken());
                max = Math.max(max, candy[i]);
            }

            long low = 1L;
            long high = max;
            long ans = 0;
            while (low <= high) {
                long mid = (low + high) / 2;
                // 가방을 mid 개 만큼 만들 것이라고 결정했다.
                
                // 각 가방에 최대 몇 개의 사탕을 넣을 수 있는 지
                long sum = 0L;
                for (int i = 0; i < N; i++) {
                    sum += (candy[i] / mid);
                }
                if (sum < M) {
                    high = mid - 1;
                } else {
                    ans = mid;
                    low = mid + 1;
                }
            }
            bw.append("#" + tc + " " + ans + "\n");
        }
        bw.flush();
    }
}