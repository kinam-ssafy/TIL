'''swea5105 미로의 거리
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    def find_start(arr):    #시작점 찾아서 반환
        ci, cj = None, None
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == 2:  #시작점이면
                    ci, cj = i, j   #현재 i j에 저장

        return [ci, cj]

    def bfs(arr):
        N = len(arr)
        di = [0, 1, 0, -1]  #인접 칸 탐색 위한 델타 선언
        dj = [1, 0, -1, 0]

        visited = [[0]*N for _ in range(N)] #방문리스트
        start = find_start(arr) #시작점 [ci, cj] 할당
        q = []  #큐 선언
        q = [start]
        visited[start[0]][start[1]] = 1   #시작점을 방문 리스트에 추가

        while q:
            ti, tj = q.pop(0)
            #visit(t)
            if arr[ti][tj] == 3:    #목적지 도착하면?
                return visited[ti][tj]-2  #거리정보 반환, 시작점과 도착지점에서 1 씩 증가하니 총 2를 뺴줘야함
            
            for ni, nj in zip(di, dj):
                fi, fj = ti+ni, tj+nj #다음 탐색할 인덱스
                #배열 범위, 벽이 아닌지, 방문했었는지의 조건
                if 0 <= fi < N and 0 <= fj < N and arr[fi][fj] != 1 and visited[fi][fj] == 0:
                    visited[fi][fj] = visited[ti][tj] + 1 #거리정보 
                    q.append([fi, fj])

        return 0 #목적지 도착 못하고 while문 끝나버리면 길이 끊겨있는 것이므로 0 반환
            
    print(f"#{t} {bfs(maze)}")
