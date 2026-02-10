import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
class Solution
{
    static char[] arr;
    static int n;
    static StringBuilder sb = new StringBuilder();
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
        for(int tc = 1 ; tc <= 10 ; tc++) {
            sb.append("#" + tc + " ");
             
            n = Integer.parseInt(br.readLine());
             
            arr = new char[n + 1];
             
            for(int i = 1 ; i <= n ; i++) {
                arr[i] = br.readLine().split(" ")[1].charAt(0);
            }
            dfs(1);
            sb.append("\n");
        }
        System.out.println(sb);
    }
     
    public static void dfs(int cur) {  // cur := 현재 탐색 중인 정점의 번호
 
        if(cur > n) return;
         
        dfs(cur*2);
        sb.append(arr[cur]);
        dfs(cur*2 + 1);
    }
}