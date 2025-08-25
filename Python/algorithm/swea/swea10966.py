'''swea10966 물놀이를 가자
여름이 되어 물놀이를 가는 사람들이 많다. 

지도는 NxM크기의 격자로 표현이 가능하고, 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현된다.
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다. 
단, 격자 밖으로 나가는 이동은 불가능하다. 
땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 
모든 이동 횟수의 합을 출력하는 프로그램을 작성하라.
'''
# from collections import deque
# def bfs(arr, N, M):
#     di = [0, 1, 0, -1] # 상하좌우 확인 위한 델타
#     dj = [1, 0, -1, 0]

#     q = deque([])
#     visited = [[-1]*M for _ in range(N)] #거리 정보 생각하여 방문 x면 -1 로 표시
#     sum_distance = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W': #물에서 출발한다고 생각
#                 q.append([i, j])
#                 visited[i][j] = 0 #시작점 방문 표시


#     while q:
#         ti, tj = q.popleft()
        
#         for ni, nj in zip(di, dj):
#             fi, fj = ti + ni, tj + nj # 다음 탐색할 인덱스
#             #배열범위, 벽이 아닌지, 방문 했었는지
#             if 0 <= fi < N and 0 <= fj < M and visited[fi][fj] == -1:
#                 visited[fi][fj] = visited[ti][tj] + 1 #방문했다고 표시 + 거리 정보 할당
#                 q.append([fi, fj])

#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'L':
#                 sum_distance += visited[i][j]
    
#     return sum_distance

# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     beach = [input() for _ in range(N)]

#     result = bfs(beach, N, M)

#     print(f"#{t} {result}")


def bfs(arr, N, M):
    di = [0, 1, 0, -1] # 상하좌우 확인 위한 델타
    dj = [1, 0, -1, 0]

    q = [0] * 2 * N * M
    front = rear = -1
    visited = [[-1]*M for _ in range(N)] #거리 정보 생각하여 방문 x면 -1 로 표시
    sum_distance = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W': #물에서 출발한다고 생각
                rear += 1   #인큐
                q[rear] = i
                rear += 1
                q[rear] = j
                visited[i][j] = 0 #시작점 방문 표시


    while front != rear:
        #디큐
        front += 1
        ti = q[front]
        front += 1
        tj = q[front]

        for ni, nj in zip(di, dj):
            fi, fj = ti + ni, tj + nj # 다음 탐색할 인덱스
            #배열범위, 벽이 아닌지, 방문 했었는지
            if 0 <= fi < N and 0 <= fj < M and visited[fi][fj] == -1:
                rear += 1
                q[rear] = fi
                rear += 1
                q[rear] = fj
                visited[fi][fj] = visited[ti][tj] + 1 #방문했다고 표시 + 거리 정보 할당

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                sum_distance += visited[i][j]
    
    return sum_distance

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    beach = [input() for _ in range(N)]

    result = bfs(beach, N, M)

    print(f"#{t} {result}")