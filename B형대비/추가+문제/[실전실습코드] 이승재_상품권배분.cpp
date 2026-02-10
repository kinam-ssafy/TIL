#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

extern void init(int N, int mId[], int mNum[]);
extern int add(int mId, int mNum, int mParent);
extern int remove(int mId);
extern int distribute(int K);

/////////////////////////////////////////////////////////////////////////

#define CMD_INIT 1
#define CMD_ADD 2
#define CMD_REMOVE 3
#define CMD_DISTRIBUTE 4

static bool run() {
	int q;
	scanf("%d", &q);

	static int midArr[1000], mnumArr[1000];
	int mid, mnum, mparent, n, k;
	int cmd, ans, ret = 0;
	bool okay = false;

	for (int i = 0; i < q; ++i) {
		scanf("%d", &cmd);
		switch (cmd) {
			case CMD_INIT:
				scanf("%d", &n);
				for (int j = 0; j < n; ++j) {
					scanf("%d %d", &midArr[j], &mnumArr[j]);
				}
				init(n, midArr, mnumArr);
				okay = true;
				break;
			case CMD_ADD:
				scanf("%d %d %d %d", &mid, &mnum, &mparent, &ans);
				ret = add(mid, mnum, mparent);
				if (ans != ret)
					okay = false;
				break;
			case CMD_REMOVE:
				scanf("%d %d", &mid, &ans);
				ret = remove(mid);
				if (ans != ret)
					okay = false;
				break;
			case CMD_DISTRIBUTE:
				scanf("%d %d", &k, &ans);
				ret = distribute(k);
				if (ans != ret)
					okay = false;
				break;
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

unordered_map<int, int> cmp;
int C = 0;


int p[18'000];
int sub[18'000];
int deg[18'000];
int nGroup;
bool is_dead[18'000];
void init(int n, int id[], int si[]) {
	memset(is_dead, 0, sizeof is_dead);
	cmp.clear();
	C = 0;
	nGroup = n;
	for (int i = 0; i < n; ++i) {
		int my = cmp[id[i]] = C++;
		p[my] = -1;
		sub[my] = si[i];
		deg[my] = 0;
	}
}

int add(int id, int si, int par) {
	par = cmp[par];
	if (deg[par] >= 3) {
		return -1;
	}
	id = cmp[id] = C++;
	deg[par]++;
	p[id] = par;
	sub[id] = 0;
	deg[id] = 0;
	while (id != -1) {
		sub[id] += si;
		id = p[id];
	}
	return sub[par];
}

int remove(int id) {
	if (!cmp.count(id)) {
		return -1;
	}
	id = cmp[id];	
	for (int node = id; node != -1; node = p[node]) {
		if (is_dead[node]) {
			return -1;
		}
	}
	is_dead[id] = true;
	deg[p[id]]--;
	int si = sub[id];
	while (id != -1) {
		sub[id] -= si;
		id = p[id];
	}
	return si;
}
int distribute(int K) {
	vector<int> si(sub, sub + nGroup);
	sort(si.begin(), si.end());
	int pref = accumulate(si.begin(), si.end(), 0);
	if (pref <= K) return si.back();
	for (int i = nGroup - 1; i >= 0; --i) {
		pref -= si[i];
		int L = (K - pref) / (nGroup - i);
		if ((i - 1 >= 0 ? si[i - 1] : 0) <= L) {
			return L;
		}
	}
	return 0;
}