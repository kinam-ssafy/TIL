#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define MAX_ROW 40
#define MAX_COL 30

struct Result{
    int row;
    int col;
};

void init(int mRows, int mCols, int mCells[MAX_ROW][MAX_COL]);
Result putPuzzle(int mPuzzle[3][3]);
void clearPuzzles();


#define CMD_INIT 1
#define CMD_PUT 2
#define CMD_CLR 3


static bool run()
{
    int query_num;
    scanf("%d", &query_num);

    bool ok = false;

    for (int q = 0; q < query_num; q++)
    {
        int query;
        scanf("%d", &query);
        if (query == CMD_INIT)
        {
            int mRows, mCols;
            int mCells[MAX_ROW][MAX_COL];
            scanf("%d %d", &mRows, &mCols);
            for (int i = 0; i < mRows; i++){
                for (int j = 0; j < mCols; j++){
                    scanf("%d", &mCells[i][j]);
                }
            }
            init(mRows, mCols, mCells);
            ok = true;
        }
        else if (query == CMD_PUT)
        {
            char strPuzzle[10];
            int mPuzzle[3][3];
            int ans_row, ans_col;
            scanf("%s", strPuzzle);
            int cnt = 0;
            for (int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++){
                    mPuzzle[i][j] = strPuzzle[cnt] - '0';
                    cnt++;
                }
            }
            Result ret = putPuzzle(mPuzzle);
            scanf("%d %d", &ans_row, &ans_col);
            if (ans_row != ret.row || ans_col != ret.col)
            {
                ok = false;
            }
        }
        else if (query == CMD_CLR)
        {
            clearPuzzles();
        }
    }
    return ok;
}


int main()
{
    setbuf(stdout, NULL);
    // freopen("sample_input.txt", "r", stdin);
    int T, MARK;
    scanf("%d %d", &T, &MARK);
    for (int tc = 1; tc <= T; tc++)
    {
        int score = run() ? MARK : 0;
        printf("#%d %d\n", tc, score);
    }
    return 0;
}
/*
1. delta equal
2. not overlap
3. 행이 작을수록, 열이 작을수록
4. 못 놓으면 제거
*/
#define MAX_ROW 40
#define MAX_COL 30
#include <bits/stdc++.h>
using namespace std;
constexpr int inf = (int)1e9 + 7;
const vector<vector<pair<int, int>>> pattern = {
	{{0, 0}, {1, 0}, {1, 1}, {1, 2}, {2, 2}},
	{{0, 0}, {0, 1}, {1, 1}, {1, 2}},
	{{0, 0}, {0, 1}, {0, 2}},
	{{0, 0}, {1, 0}, {2, 0}},
	{{0, 0}, {0, 1}}
};

struct D {
	int type, hash;
	vector<pair<int, int>> p;
};
vector<D> ds;
vector<pair<int, int>> ps;
int H, W;
vector<pair<int, int>> pq[5][1 << 15];
bitset<30> on[40];
void init(int h, int w, int grid[MAX_ROW][MAX_COL]) {
	H = h, W = w;
	for (int i = 0; i < h; ++i) {
		on[i].reset();
	}
	ds.clear();
	for (auto &[u, v]: ps) {
		pq[u][v].clear();
	}
	ps.clear();
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			for (int type = 0; type < 5; ++type) {
				int mn = inf;
				bool good = true;
				for (auto &[di, dj]: pattern[type]) {
					if (i + di >= h || j + dj >= w) {
						good = false;
						break;
					}
					mn = min(mn, grid[i + di][j + dj]);
				}
				if (!good) continue;
				int hash = 0;
				for (auto &[di, dj]: pattern[type]) {
					int delta = grid[i + di][j + dj] - mn;
					hash <<= 3;
					hash += delta;
				}
				pq[type][hash].push_back({i, j});
				ps.push_back({type, hash});
			}
		}
	}
	sort(ps.begin(), ps.end());
	ps.resize(unique(ps.begin(), ps.end()) - ps.begin());
	for (auto &[u, v]: ps) {
		sort(pq[u][v].rbegin(), pq[u][v].rend());
		ds.push_back({u, v, pq[u][v]});
	}
}

Result putPuzzle(int pz[3][3]) {
    int type = -1;
	for (int t = 0; t < 5; ++t) {
		bool good = true;
		for (auto &[di, dj]: pattern[t]) {
			if (pz[di][dj] == 0) {
				good = false;
				break;
			}
		}
		if (good) {
			type = t;
			break;
		}
	}
	int mn = inf;
	for (auto &[di, dj]: pattern[type]) {
		mn = min(mn, pz[di][dj]);
	}
	int hash = 0;
	for (auto &[di, dj]: pattern[type]) {
		int delta = pz[di][dj] - mn;
		hash <<= 3;
		hash += delta;
	}
	auto &p = pq[type][hash];
	Result res = {-1, -1};
	while (!p.empty()) {
		auto [r, c] = p.back(); p.pop_back();
		bool good = true;
		for (auto &[di, dj]: pattern[type]) {
			if (on[r + di].test(c + dj)) {
				good = false;
				break;
			}
		}
		if (!good) continue;
		res = {r, c};
		for (auto &[di, dj]: pattern[type]) {
			on[r + di].set(c + dj);
		}
		break;
	}
	return res;
}

void clearPuzzles() {
    for (int i = 0; i < H; ++i) {
		on[i].reset();
	}
	for (auto &[r, c, p]: ds) {
		pq[r][c] = p;
	}
}