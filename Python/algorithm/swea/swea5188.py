'''swea5188 최소합 완전탐색
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 
최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 
가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
'''

def dfs(ci, cj, sum):
    global min_sum

    if min_sum <= sum:
        return

    if ci == (N - 1) and cj == (N - 1):
        min_sum = min(min_sum, sum)
        return min_sum

    for ni, nj in zip(di, dj):
        fi, fj = ci + ni, cj + nj
        if 0 <= fi < N and 0 <= fj < N:
            dfs(fi, fj, sum + arr[fi][fj])

    return min_sum



T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1]
    dj = [1, 0]

    min_sum = float('inf')
    result = dfs(0, 0, arr[0][0])

    print(f"#{t} {result}")

