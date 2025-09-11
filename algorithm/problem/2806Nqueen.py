'''swea2806 N queen
8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.

퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 이 문제의 한가지 정답은 아래 그림과 같다.

이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.

N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''
def visit(row, col):
    visited = []
    if arr[row][col] == 0:
            #방문표시
            for dir in range(8):
                for n in range(N):
                    ni, nj = row + di[dir] * n, col + dj[dir] * n
                    if 0 <= ni < N and 0 <= nj < N:
                        if not arr[ni][nj]:
                            arr[ni][nj] = 1
                            visited.append([ni, nj])

    
    return visited

def backtrac(li):
    for ni, nj in li:
        arr[ni][nj] = 0


def dfs(row):
    if row == N:
        return 1
    
    cnt = 0

    for col in range(N):
        if arr[row][col] == 0:
            #방문표시
            visited_list = visit(row, col)

            cnt += dfs(row + 1)

            #백트래킹
            backtrac(visited_list)

    return cnt


T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]

    ans = dfs(0)
    print(f"#{t} {ans}")