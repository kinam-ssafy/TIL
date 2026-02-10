import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
class  Solution{
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T;
        T= Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
 
            int lastNBit = (1 << (N)) - 1;  // 111...1 (길이 N)
            if( lastNBit == (M & lastNBit)){
                System.out.println("#" + test_case + " " + "ON");
            }else{
                System.out.println("#" + test_case + " " + "OFF");
            }
        }
    }
}