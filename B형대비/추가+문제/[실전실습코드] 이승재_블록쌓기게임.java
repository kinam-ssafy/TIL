import java.io.*;
import java.util.*;
class Solution {
    private static BufferedReader br;
    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT = 100;
    private final static int CMD_DROP = 200;
	
	
	public static final class Result{
		int top;
		int count;

		Result(){
			top = 0;
			count = 0;
		}
	}

    private static boolean run() throws Exception {

        StringTokenizer stdin = new StringTokenizer(br.readLine(), " ");

        int query_num = Integer.parseInt(stdin.nextToken());
		int ans_top, ans_count;
        boolean ok = false;

        for (int q = 0; q < query_num; q++) {
            stdin = new StringTokenizer(br.readLine(), " ");
            int query = Integer.parseInt(stdin.nextToken());

            if (query == CMD_INIT) {
                int C = Integer.parseInt(stdin.nextToken());
                usersolution.init(C);
                ok = true;
            } else if (query == CMD_DROP) {
                int mCol = Integer.parseInt(stdin.nextToken());
                int mHeight = Integer.parseInt(stdin.nextToken());
                int mLength = Integer.parseInt(stdin.nextToken());
				
				Result ret = usersolution.dropBlocks(mCol, mHeight, mLength);
                ans_top = Integer.parseInt(stdin.nextToken());
				ans_count = Integer.parseInt(stdin.nextToken());
                
                if (ans_top != ret.top || ans_count != ret.count) {
                    ok = false;
                }
            }
        }
        return ok;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;

        // System.setIn(new java.io.FileInputStream("res/sample_input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stinit = new StringTokenizer(br.readLine(), " ");
        T = Integer.parseInt(stinit.nextToken());
        MARK = Integer.parseInt(stinit.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }

        br.close();
    }
}

class UserSolution {
	int[] a;
	int[] m;
	int[] M;
	long tot;
	int col;
    void init(int C) {
		int p2 = 1;
		while (p2 < C) p2 *= 2;
		a = new int[p2 * 2];
		m = new int[p2 * 2];
		M = new int[p2 * 2];
		tot = 0;
		col = C;
    }
	void range_update(int qs, int qe, int qk, int ns, int ne, int nx) {
		if (qe < ns || ne < qs) return;
		if (qs <= ns && ne <= qe) {
			a[nx] += qk; m[nx] += qk; M[nx] += qk;
		} else {
			int mid = (ns + ne) / 2;
			range_update(qs, qe, qk, ns, mid, nx * 2);
			range_update(qs, qe, qk, mid + 1, ne, nx * 2 + 1);
			m[nx] = Math.min(m[nx * 2], m[nx * 2 + 1]) + a[nx];
			M[nx] = Math.max(M[nx * 2], M[nx * 2 + 1]) + a[nx];
		}
	}

    Solution.Result dropBlocks(int c, int height, int length) {
        Solution.Result ret = new Solution.Result();
		tot += height * length;
        range_update(c, c + length - 1, height, 0, col - 1, 1);
		int mn = m[1], mx = M[1];
		ret.top = mx - mn;
		ret.count = (int)((tot - 1L * mn * col) % 1000000);
		return ret;
    }
}