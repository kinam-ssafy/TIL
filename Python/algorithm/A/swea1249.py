'''swea1249 보급로
출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.
도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.

출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.

깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다.

이동 경로는 상하좌우 방향으로 진행할 수 있으며, 한 칸씩 움직일 수 있다.

지도 정보에는 각 칸마다 파여진 도로의 깊이가 주어진다. 
현재 위치한 칸의 도로를 복구해야만 다른 곳으로 이동할 수 있다.
출발지에서 도착지까지 거리에 대해서는 고려할 필요가 없다.

'''

from collections import deque

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    start = [0, 0] # 시작점
    q = deque([start])
    visited[0][0] = 0 # 시작점 방문표시
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while q:
        ti, tj = q.popleft()

        if ti == N-1 and tj == N-1:
            print(f"#{t} {visited[ti][tj] - 1}")
            break

        for ni, nj in zip(di, dj):
            fi, fj = ti+ni, tj+nj

            if 0 <= fi < N and 0 <= fj < N and arr[fi][fj] in list(range(10)):
                visited[fi][fj] = visited[ti][tj] + arr[fi][fj]
                q.append([fi, fj])

            
            
