from collections import deque

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]

def isZero(r, c):
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue

        if arr[nr][nc] == -2:
            return False

    return True

def click(r, c):
    q = deque()
    q.append([r, c])
    arr[r][c] = 0
    while len(q) > 0:
        cur = q[0]
        q.popleft()

        arr[cur[0]][cur[1]] = 0
        for i in range(8):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc] != -1:
                continue

            if isZero(nr, nc):
                q.append([nr, nc])

            arr[nr][nc] = 0

def solve():
    global ans

    for i in range(N):
        for j in range(N):
            if arr[i][j] != -1:
                continue

            if isZero(i, j):
                click(i, j)
                ans += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1:
                ans += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [['' for _ in range(N)] for _ in range(N)]

    ans = 0
    for i in range(N):
        s = input()
        for j in range(N):
            if s[j] == '.':
                arr[i][j] = -1
            else:
                arr[i][j] = -2

    solve()
    print(f'#{tc} {ans}')