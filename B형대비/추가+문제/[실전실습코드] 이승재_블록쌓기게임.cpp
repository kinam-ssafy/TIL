#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

struct Result
{
    int top;
    int count;
};

void init(int C);
Result dropBlocks(int mCol, int mHeight, int mLength);

#define CMD_INIT 100
#define CMD_DROP 200

static bool run()
{
    int query_num;
    scanf("%d", &query_num);

    int ans_top, ans_count;
    bool ok = false;

    for (int q = 0; q < query_num; q++)
    {
        int query;
        scanf("%d", &query);
        if (query == CMD_INIT)
        {
            int C;
            scanf("%d", &C);
            init(C);
            ok = true;
        }
        else if (query == CMD_DROP)
        {
            int mCol, mHeight, mLength;
            scanf("%d %d %d", &mCol, &mHeight, &mLength);
            Result ret = dropBlocks(mCol, mHeight, mLength);
            scanf("%d %d", &ans_top, &ans_count);
            if (ans_top != ret.top || ans_count != ret.count)
            {
                ok = false;
            }
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

#include <bits/stdc++.h>
using namespace std;
 
constexpr int base = 1 << 20;
int add[base << 1];
int min_value[base << 1];
int max_value[base << 1];
int col;
template<int qk> void range_update(int qs, int qe, int ns = 0, int ne = -1, int nx = 1) {
    if (ne == -1) ne = col - 1;
    if (qe < ns || ne < qs) return;
    if (qs <= ns && ne <= qe) {
        add[nx] += qk;
		min_value[nx] += qk;
		max_value[nx] += qk;
    } else {
        int mid = (ns + ne) / 2;
        range_update<qk>(qs, qe, ns, mid, nx * 2);
        range_update<qk>(qs, qe, mid + 1, ne, nx * 2 + 1);
        min_value[nx] = min(min_value[nx * 2], min_value[nx * 2 + 1]) + add[nx];
        max_value[nx] = max(max_value[nx * 2], max_value[nx * 2 + 1]) + add[nx];
    }
}
long long tot = 0;
void init(int C) {
    tot = 0;
    memset(add, 0, sizeof add);
    memset(min_value, 0, sizeof min_value);
    memset(max_value, 0, sizeof max_value);
    col = C;
}
Result dropBlocks(int mCol, int mHeight, int mLength) {
    Result ret;
    ret.top = 0;
    ret.count = 0;
    tot += mHeight * mLength;

    if (mHeight == 1) range_update<1>(mCol, mCol + mLength - 1);
    if (mHeight == 2) range_update<2>(mCol, mCol + mLength - 1);
    if (mHeight == 3) range_update<3>(mCol, mCol + mLength - 1);
    int mn = min_value[1];
    int mx = max_value[1];
    ret.top = mx - mn;
    ret.count = (tot - 1LL * mn * col) % 1'000'000;
    return ret;
}