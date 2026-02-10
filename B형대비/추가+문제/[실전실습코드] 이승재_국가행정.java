// package swexpert.country;

import java.util.*;

class Solution {
	private static final int CMD_INIT = 100;
	private static final int CMD_EXPAND = 200;
	private static final int CMD_CALCULATE = 300;
	private static final int CMD_DIVIDE = 400;
	private static final int MAX_N = 10000;

	private static int[] population = new int[MAX_N];
	private static UserSolution usersolution = new UserSolution();
	private static Scanner sc;

	private static boolean run() throws Exception {
		boolean okay = false;
		int Q = sc.nextInt();

		for (int q = 0; q < Q; ++q) {
			int ret, ans, N, from, to, num;
			int cmd = sc.nextInt();

			switch (cmd) {
				case CMD_INIT:
					N = sc.nextInt();
					for (int i = 0; i < N; i++) {
						int in = sc.nextInt();
						population[i] = in;
					}
					usersolution.init(N, population);
					okay = true;
					break;
				case CMD_EXPAND:
					num = sc.nextInt();
					ret = usersolution.expand(num);
					ans = sc.nextInt();
					if (ret != ans)
						okay = false;
					break;
				case CMD_CALCULATE:
					from = sc.nextInt();
					to = sc.nextInt();
					ret = usersolution.calculate(from, to);
					ans = sc.nextInt();
					if (ret != ans)
						okay = false;
					break;
				case CMD_DIVIDE:
					from = sc.nextInt();
					to = sc.nextInt();
					num = sc.nextInt();
					ret = usersolution.divide(from, to, num);
					ans = sc.nextInt();
					if (ret != ans)
						okay = false;
					break;
				default:
					okay = false;
					break;
			}
		}

		return okay;
	}

	public static void main(String[] args) throws Exception {
		// System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

		sc = new Scanner(System.in);

		int TC = sc.nextInt();
		int MARK = sc.nextInt();

		for (int testcase = 1; testcase <= TC; ++testcase) {
			int score = run() ? MARK : 0;
			System.out.println("#" + testcase + " " + score);
		}

		sc.close();
	}
}

class UserSolution {
	private int base;
	private int[] seg;
	private int[] population;
	private int[] C;
	private PriorityQueue<PqEdge> pq;

	private class PqEdge implements Comparable<PqEdge> {
		int index, weight;

		PqEdge(int index, int weight) {
			this.index = index;
			this.weight = weight;
		}

		@Override
		public int compareTo(PqEdge other) {
			if (this.weight != other.weight)
				return Integer.compare(other.weight, this.weight);
			else
				return Integer.compare(this.index, other.index);
		}
	}

	public void update(int index, int value) {
		seg[index += base] = value;
		while ((index >>= 1) > 0)
			seg[index] = seg[index * 2] + seg[index * 2 + 1];
	}

	public int getSum(int qs, int qe) {
		int ret = 0;
		for (qs += base, qe += base; qs <= qe; qs >>= 1, qe >>= 1) {
			if (qs % 2 == 1)
				ret += seg[qs++];
			if (qe % 2 == 0)
				ret += seg[qe--];
		}
		return ret;
	}

	public void init(int N, int[] mPopulation) {
		population = mPopulation;
		pq = new PriorityQueue<>();
		base = 1;
		while (base < N)
			base *= 2;
		seg = new int[base * 2];
		C = new int[N];
		for (int i = 0; i + 1 < N; ++i) {
			C[i] = 1;
			int weight = (mPopulation[i] + mPopulation[i + 1]);
			pq.add(new PqEdge(i, weight));
			seg[base + i] = weight;
		}
		for (int i = base - 1; i > 0; --i) {
			seg[i] = seg[i * 2] + seg[i * 2 + 1];
		}
	}

	public int expand(int M) {
		int newWeight = -1;
		while (M-- > 0) {
			PqEdge top = pq.poll();
			if (top != null) {
				int index = top.index;
				++C[index];
				newWeight = (population[index] + population[index + 1]) / C[index];
				pq.add(new PqEdge(index, newWeight));
				update(index, newWeight);
			}
		}
		return newWeight;
	}

	public int calculate(int from, int to) {
		if (from > to) {
			int temp = from;
			from = to;
			to = temp;
		}
		return getSum(from, to - 1);
	}
	public int divide(int from, int to, int K) {
        int lf = 1, rg = (int)1e7;
        while (lf < rg) {
            int mid = (lf + rg) / 2;
            int P = 0;
            for (int i = from; i <= to && P <= K; ++P) {
                int sum = 0, j = i;
                while (j <= to && sum + population[j] <= mid) {
                    sum += population[j++];
                }
                i = j;
            }
            if (P <= K) {
                rg = mid;
            } else {
                lf = mid + 1;
            }
        }
        return rg;
    }
}