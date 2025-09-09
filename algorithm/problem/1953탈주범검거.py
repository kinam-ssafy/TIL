'''swea1953 탈주범검거
교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.

탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,

지하 터널 어딘가에서 은신 중인 것으로 추정된다.

터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.

탈주범은 시간당 1의 거리를 움직일 수 있다.

지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.
'''

'''
터널 구조물
1은 2 3 4 5 6 7 이랑 연결 가능
2 : 1 4(상하) 5(상하) 6(상하) 7(상하)
3 : 1  4567 좌우
4 : 1 상 2 5 6 우 3 6 7 
5 : 1 하 2 4 7 우 3 6 7 
6 : 1 하 2 4 7 좌 3 4 5 
7 : 1 상 2 5 6 좌 3 4 5 
'''
from collections import deque

def bfs(R, C):
    q = deque([(R, C)])   #후보군 튜플이 더 빠름
    visited[R][C] = 1   #출발점 초기화 

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        for dir in range(4):  #상하좌우 확인
            # 출구가 없으면 다음 방향 확인
            if dirs[dir] == 0:
                continue

            # 다음 좌표
            new_y, new_x =  now_y + dy[dir], now_x + dx[dir]


            # 범위 밖이면 pass
            if not (0 <= new_y < N and 0 <= new_x < M):
                continue

            # 못가는 못이면 pass
            if graph[new_y][new_x] == 0:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]
            #상 하 좌 우
            # 현재 상좌 -> next_dirs가 하우 가 안뚫렸으면 못감
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue

            # 현재 하우 -> next_dirs가 상좌 가 안뚫렸으면 못감
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            if visited[now_y][now_x] + 1 > L:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))



T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    #세로 크기 N, 가로 크기 M, 맨홀 뚜껑 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는지 기록
    visited = [[0] * M for _ in range(N)]

    #상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    types = {
        1: [1, 1, 1, 1],
        2: [1, 1, 0, 0],
        3: [0, 0, 1, 1],
        4: [1, 0, 0, 1],
        5: [0, 1, 0, 1],
        6: [0, 1, 1, 0],
        7: [1, 0, 1, 0]
    }

    bfs(R, C)   #출발지 입력
    cnt = 0

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f"#{tc} {cnt}")