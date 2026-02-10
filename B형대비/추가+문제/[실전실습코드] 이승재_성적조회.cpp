#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

extern void init();
extern int add(int mId, int mGrade, char mGender[7], int mScore);
extern int remove(int mId);
extern int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][7], int mScore);

/////////////////////////////////////////////////////////////////////////

#define CMD_INIT 100
#define CMD_ADD 200
#define CMD_REMOVE 300
#define CMD_QUERY 400

static bool run() {
	int q;
	scanf("%d", &q);

	int id, grade, score;
	char gender[7];
	int cmd, ans, ret;
	bool okay = false;

	for (int i = 0; i < q; ++i) {
		scanf("%d", &cmd);
		switch (cmd) {
			case CMD_INIT:
				init();
				okay = true;
				break;
			case CMD_ADD:
				scanf("%d %d %s %d %d", &id, &grade, gender, &score, &ans);
				ret = add(id, grade, gender, score);
				if (ans != ret)
					okay = false;
				break;
			case CMD_REMOVE:
				scanf("%d %d", &id, &ans);
				ret = remove(id);
				if (ans != ret)
					okay = false;
				break;
			case CMD_QUERY: {
				int gradeCnt, genderCnt;
				int gradeArr[3];
				char genderArr[2][7];
				scanf("%d", &gradeCnt);
				if (gradeCnt == 1) {
					scanf("%d %d", &gradeArr[0], &genderCnt);
				} else if (gradeCnt == 2) {
					scanf("%d %d %d", &gradeArr[0], &gradeArr[1], &genderCnt);
				} else {
					scanf("%d %d %d %d", &gradeArr[0], &gradeArr[1], &gradeArr[2], &genderCnt);
				}
				if (genderCnt == 1) {
					scanf("%s %d %d", genderArr[0], &score, &ans);
				} else {
					scanf("%s %s %d %d", genderArr[0], genderArr[1], &score, &ans);
				}
				ret = query(gradeCnt, gradeArr, genderCnt, genderArr, score);
				if (ans != ret)
					okay = false;
				break;
			}
			default:
				okay = false;
				break;
		}
	}
	return okay;
}

int main() {
	setbuf(stdout, NULL);
	//freopen("sample_input.txt", "r", stdin);

	int T, MARK;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++) {
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}

	return 0;
}
#include <bits/stdc++.h>
using namespace std;
struct student {
	int id, score;
};
bool operator<(const student &a, const student &b) {
	if (a.score != b.score) return a.score < b.score;
	return a.id < b.id;
}
set<student> st[3][2];
unordered_map<int, tuple<int, int, int>> tps;
void init() {
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 2; ++j) {
			st[i][j].clear();
		}
	}
	tps.clear();
	return;
}

int add(int mId, int mGrade, char mGender[7], int mScore) {
	--mGrade;
	auto &au = st[mGrade][mGender[0] == 'f'];
	au.insert({mId, mScore});
	tps[mId] = {mGrade, mGender[0] == 'f', mScore};
	return au.rbegin()->id;
}

int remove(int mId) {
	if (tps.count(mId) == 0) {
		return 0;
	}
	int grade, gender, score;
	tie(grade, gender, score) = tps[mId];
	auto &au = st[grade][gender];
	au.erase({mId, score});
	tps.erase(mId);
	if (au.empty()) return 0;
	return au.begin()->id;
}

int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][7], int mScore) {
	student ret{0, (int)1e9};
	for (int i = 0; i < mGradeCnt; ++i) {
		--mGrade[i];
		for (int j = 0; j < mGenderCnt; ++j) {
			auto &au = st[mGrade[i]][mGender[j][0] == 'f'];
			auto it = au.lower_bound({0, mScore});
			if (it != au.end()) {
				if (*it < ret) {
					ret = *it;
				}
			}
		}
	}
	return ret.id;
}