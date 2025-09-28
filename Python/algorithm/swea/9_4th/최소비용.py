'''swea5250 최소비용
출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.
'''
from heapq import heappop, heappush

def dijkstra(i, j):
    q = [(0, i, j)]
    cost[i][j] = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while q:
        w, ci, cj = heappop(q)

        if w > cost[ci][cj]:
            continue
        
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                nw = w + 1
                if arr[ni][nj] > arr[ci][cj]:
                    nw += arr[ni][nj] - arr[ci][cj]

                if cost[ni][nj] > nw:
                    cost[ni][nj] = nw
                    heappush(q, (nw, ni, nj))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cost = [[float('inf')] * N for _ in range(N)]
    
    dijkstra(0, 0)
    ans = cost[N-1][N-1]
    print(f"#{t} {ans}")

