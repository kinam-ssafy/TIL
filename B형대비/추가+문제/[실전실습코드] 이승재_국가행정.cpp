#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <bits/stdc++.h>
using namespace std;
template<typename A,typename B>
string to_string(pair<A,B>p){return"("+to_string(p.first)+", "+to_string(p.second)+")";}
template<typename A,typename B,typename C>
string to_string(tuple<A,B,C>p){return"("+to_string(get<0>(p))+", "+to_string(get<1>(p))+", "+to_string(get<2>(p))+")";}
template<typename A,typename B,typename C,typename D>
string to_string(tuple<A,B,C,D>p){return"("+to_string(get<0>(p))+", "+to_string(get<1>(p))+", "+to_string(get<2>(p))+", "+to_string(get<3>(p))+")";}
string to_string(const string &s){return'"'+s+'"';}
string to_string(const char *s){return to_string((string)s);}
string to_string(bool b){return(b?"true":"false");}
string to_string(char c){return string(1, c);}
string to_string(vector<bool>v){int f=0;string r="{";for(bool i:v)r+=(f++?",":"")+to_string(i);r+="}";return r;}
template<size_t N>
string to_string(bitset<N>v){string res="";for(size_t i=0;i<N;)res+=char('0'+v[i++]);return res;}
template<typename A>
string to_string(A v){int f=0;string r="{";for(auto&i:v)r+=(f++?",":"")+to_string(i);r+="}";return r;}
void debug_out(){cerr<<']'<<endl;}
template<typename Head,typename...Tail>
void debug_out(Head H,Tail...T){cerr<<to_string(H);if(sizeof...(T))cerr<<", ";debug_out(T...);}
#ifdef LOCAL
#define debug(x...) cerr << "[" << (#x) << "] = [", debug_out(x)
#else
#define debug(x...) 33
#endif
#include <stdio.h>

extern void init(int N, int mPopulation[]);
extern int expand(int M);
extern int calculate(int mFrom, int mTo);
extern int divide(int mFrom, int mTo, int K);

/////////////////////////////////////////////////////////////////////////

#define MAX_N				10000

#define CMD_INIT			100
#define CMD_EXPAND			200
#define CMD_CALCULATE		300
#define CMD_DIVIDE			400

static bool run()
{
	int population[MAX_N];
	int cmd, ans, ret;
	int Q = 0;
	int N, from, to, num;
	bool okay = false;

	scanf("%d", &Q);

	for (int q = 0; q < Q; ++q)
	{
		scanf("%d", &cmd);

		switch (cmd)
		{
		case CMD_INIT:
			scanf("%d", &N);

			for (int i = 0; i < N; i++)
				scanf("%d", &population[i]);

			init(N, population);
			okay = true;
			break;

		case CMD_EXPAND:
			scanf("%d", &num);
			ret = expand(num);
			scanf("%d", &ans);
			if (ret != ans) {
				debug("expand", ans, ret);
				okay = false;
				exit(0);
			}
			break;

		case CMD_CALCULATE:
			scanf("%d %d", &from, &to);
			ret = calculate(from, to);
			scanf("%d", &ans);
			if (ret != ans) {
				debug("calc", ans, ret);
				okay = false;
				exit(0);
			}
			break;

		case CMD_DIVIDE:
			scanf("%d %d %d", &from, &to, &num);
			ret = divide(from, to, num);
			scanf("%d", &ans);
			if (ret != ans) {
				debug("div", ans, ret);
				okay = false;
				exit(0);
			}
			break;

		default:
			okay = false;
		}
	}

	return okay;
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

int base;
int seg[1 << 15];
void update(int index, int value) {
	seg[index += base] = value;
	while (index >>= 1) seg[index] = seg[index * 2] + seg[index * 2 + 1];
}
int get_sum(int qs, int qe) {
	int ret = 0;
	for (qs += base, qe += base; qs <= qe; qs >>= 1, qe >>= 1) {
		if (qs % 2 == 1) ret += seg[qs++];
		if (qe % 2 == 0) ret += seg[qe--];
	}
	return ret;
}
struct pq_edge {
	int index, weight;
};
bool operator<(const pq_edge &a, const pq_edge &b) {
	if (a.weight != b.weight) return a.weight < b.weight;
	else return a.index > b.index;
}

priority_queue<pq_edge> pq;
int *population;
int C[10'000];

void init(int N, int mPopulation[]) {
	population = mPopulation;
	pq = priority_queue<pq_edge>();
	base = 1;
	while (base < N - 1) base *= 2;
	for (int i = 0; i + 1 < N; ++i) {
		C[i] = 1;
		int weight = (mPopulation[i] + mPopulation[i + 1]);
		pq.push({i, weight});
		seg[base + i] = weight;
	}
	for (int i = base - 1; i > 0; --i) {
		seg[i] = seg[i * 2] + seg[i * 2 + 1];
	}
}
int expand(int M) {
	int new_weight = -1;
	while (M--) {
		auto [index, weight] = pq.top(); pq.pop();
		++C[index];
		new_weight = (population[index] + population[index + 1]) / C[index];
		pq.push({index, new_weight});
		update(index, new_weight);
	}
	return new_weight;
}

int calculate(int from, int to) {
	if (from > to) swap(from, to);
	return get_sum(from, to - 1);
}

int divide(int from, int to, int K) {
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