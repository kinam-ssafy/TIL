'''swea5250 최소비용

출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 
최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 
각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

(표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 
더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

색이 칠해진 칸을 따라 이동하는 경우 기본적인 연료 소비량 4에, 
높이가 0에서 1로 경우만큼 추가 연료가 소비되므로 최소 연료 소비량 5로 목적지에 도착할 수 있다.

이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.


첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.

1<=T<=50, 3<=N<=100, 0<=H<1000
'''

def dijkstra(start_i, start_j):
    pq = [(0, start_i, start_j)]
    dists = [[INF] * N for _ in range(N)]
    dists[start_i][start_j] = 0 

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while pq:
        dist, ci, cj = heappop(pq)

        if dists[ci][cj] < dist:
            continue

        for dir in range(4):
            ni, nj = ci + di[dir], cj + dj[dir]
            if 0 <= ni < N and 0 <= nj < N:
                new_dist = dist + 1 # 기본적으로 한 칸 이동 시 1씩 늘어남
                if arr[ci][cj] < arr[ni][nj]:   #계단이 있는 경우
                    new_dist += arr[ni][nj] - arr[ci][cj]   #높이 차이만큼 더해줌

                if dists[ni][nj] > new_dist:    #새로운 거리정보가 기존 거리정보보다 작으면
                    dists[ni][nj] = new_dist    # 갱신해줌
                    heappush(pq, (new_dist, ni, nj))

    return dists[N-1][N-1]  # 도착 지점에 저장된 거리 정보 리턴


from heapq import heappop, heappush
INF = int(1000000) # 최댓값 설정


T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 추가 소비되는 연료가 저장될 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(0, 0)
    print(f"#{t} {result}")