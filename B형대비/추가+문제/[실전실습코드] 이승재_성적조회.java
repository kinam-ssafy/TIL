import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.*;

class Solution {
	private final static int CMD_INIT = 100;
	private final static int CMD_ADD = 200;
	private final static int CMD_REMOVE = 300;
	private final static int CMD_QUERY = 400;

	private final static UserSolution usersolution = new UserSolution();

	private static void String2Char(char[] buf, String str) {
		for (int k = 0; k < str.length(); ++k)
			buf[k] = str.charAt(k);
		buf[str.length()] = '\0';
	}
	private static boolean run(BufferedReader br) throws Exception {
		int q = Integer.parseInt(br.readLine());

		int id, grade, score;
		int cmd, ans, ret;
		boolean okay = false;

		for (int i = 0; i < q; ++i) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			cmd = Integer.parseInt(st.nextToken());
			switch (cmd) {
				case CMD_INIT:
					usersolution.init();
					okay = true;
					break;
				case CMD_ADD:
					char[] gender = new char[7];
					id = Integer.parseInt(st.nextToken());
					grade = Integer.parseInt(st.nextToken());
					String2Char(gender, st.nextToken());
					score = Integer.parseInt(st.nextToken());
					ans = Integer.parseInt(st.nextToken());
					ret = usersolution.add(id, grade, gender, score);
					if (ret != ans)
						okay = false;
					break;
				case CMD_REMOVE:
					id = Integer.parseInt(st.nextToken());
					ans = Integer.parseInt(st.nextToken());
					ret = usersolution.remove(id);
					if (ret != ans)
						okay = false;
					break;
				case CMD_QUERY:
					int gradeCnt, genderCnt;
					int[] gradeArr = new int[3];
					char[][] genderArr = new char[2][7];
					gradeCnt = Integer.parseInt(st.nextToken());
					for (int j = 0; j < gradeCnt; ++j) {
						gradeArr[j] = Integer.parseInt(st.nextToken());
					}
					genderCnt = Integer.parseInt(st.nextToken());
					for (int j = 0; j < genderCnt; ++j) {
						String2Char(genderArr[j], st.nextToken());
					}
					score = Integer.parseInt(st.nextToken());
					ans = Integer.parseInt(st.nextToken());
					ret = usersolution.query(gradeCnt, gradeArr, genderCnt, genderArr, score);
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
		int TC, MARK;

		//System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		TC = Integer.parseInt(st.nextToken());
		MARK = Integer.parseInt(st.nextToken());

		for (int testcase = 1; testcase <= TC; ++testcase) {
			int score = run(br) ? MARK : 0;
			System.out.println("#" + testcase + " " + score);
		}

		br.close();
	}
}

class student implements Comparable<student>{
	int id;
	int score;
	student(int id, int score) {
		this.id = id;
		this.score = score;
	}
	student() { }
	@Override
	public int compareTo(student arg0) {
		if (arg0.score != score) {
			return Integer.compare(score, arg0.score);
		} else {
			return Integer.compare(id, arg0.id);
		}
	}
}
class tuple {
	int grade, gender, score;
	tuple() { }
	tuple(int grade, int gender, int score) {
		this.grade = grade;
		this.gender = gender;
		this.score = score;
	}
}
class UserSolution {
	TreeSet<student>[][] st = new TreeSet[3][2];
	HashMap<Integer, tuple> tps;
	public void init() {
		for (int i = 0; i < 3; ++i) {
			for (int j = 0; j < 2; ++j) {
				st[i][j] = new TreeSet<>();
			}
		}
		tps = new HashMap<>();
	}

	public int add(int mId, int mGrade, char mGender[], int mScore) {
		--mGrade;
		st[mGrade][mGender[0] == 'f' ? 1 : 0].add(new student(mId, mScore));
		tps.put(mId, new tuple(mGrade, mGender[0] == 'f' ? 1 : 0, mScore));
		return st[mGrade][mGender[0] == 'f' ? 1 : 0].last().id;
	}

	public int remove(int mId) {
		if (tps.containsKey(mId) == false) return 0;
		tuple tp = tps.get(mId);
		st[tp.grade][tp.gender].remove(new student(mId, tp.score));
		tps.remove(mId);
		if (st[tp.grade][tp.gender].size() == 0) return 0;
		return st[tp.grade][tp.gender].first().id;
	}

	public int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore) {
		student ret = new student(0, (int)1e9);
		for (int i = 0; i < mGradeCnt; ++i) {
			--mGrade[i];
			for (int j = 0; j < mGenderCnt; ++j) {
				student stud = st[mGrade[i]][mGender[j][0] == 'f' ? 1 : 0].higher(new student(0, mScore));
				if (stud != null) {
					if (stud.compareTo(ret) < 0) {
						ret = stud;
					}
				}

			}
		}
		return ret.id;
	}
}