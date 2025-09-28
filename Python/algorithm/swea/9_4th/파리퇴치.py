'''swea2001 파리퇴치

N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!
'''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 1]
    dj = [1, 0, 1]

    current = 0
    ans = 0

    for i in range(N):
        for j in range(N):
            current = 0
            for p in range(M):
                for q in range(M):
                    ni, nj = i + p, j + q
                    if 0 <= ni < N and 0 <= nj < N:
                        current += arr[ni][nj]

            ans = max(ans, current)

    print(f"#{t} {ans}")
    