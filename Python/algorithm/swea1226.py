'''swea1226 미로1
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

아래의 예시에서는 도달 가능하다.
'''
def find_start(arr): # 시작점의 인덱스 찾기
    ci, cj = None, None
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2: #시작점이면
                ci, cj = i, j

    return [ci, cj]

def bfs(arr):
    N = len(arr)
    di = [0, 1, 0, -1] # 상하좌우 확인 위한 델타
    dj = [1, 0, -1, 0]

    visited = [[0]*N for _ in range(N)]
    start = find_start(arr) # 시작점 찾아서 할당

    q = [start]
    visited[start[0]][start[1]] = 1 #시작점 방문표시

    while q:
        ti, tj = q.pop(0)
        
        if arr[ti][tj] == 3: #목적지 도착하면
            return 1 #도달 가능 여부 1 반환
        
        for ni, nj in zip(di, dj):
            fi, fj = ti + ni, tj + nj # 다음 탐색할 인덱스
            #배열범위, 벽이 아닌지, 방문 했었는지
            if 0 <= fi < N and 0 <= fj < N and arr[fi][fj] != 1 and visited[fi][fj] == 0:
                visited[fi][fj] = 1 #방문했다고 표시
                q.append([fi, fj])

    return 0 #도착못하고 q 비어버리면 0 반환

for t in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    result = bfs(maze)

    print(f"#{t} {result}")
