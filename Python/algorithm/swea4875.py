'''swea4875 미로
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.

13101

10101

10101

10101

10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[] * N for _ in range(N)]
    stack = [] # 탐색 경로를 저장할 스택

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N): # 시작점과 끝점 인덱스 파악
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                stack.append(start)

            elif arr[i][j] == 3:
                end = [i, j]
            if start and end:
                isbreak = 1
                break
        if isbreak == 1:
            break

    while len(stack) >= 1:
        current_i, current_j = stack.pop()

        if arr[current_i][current_j] == 3:
            break

            for ni, nj in list(zip(di, dj)):




