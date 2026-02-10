from collections import deque

MAX_N = 20
MAX_HASH = 9999

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class Candidate:
    def __init__(self, r=0, c=0, isHorizontal=False, isReverse=False):
        self.r = r
        self.c = c
        self.isHorizontal = isHorizontal
        self.isReverse = isReverse

def init(N, mMap):
    global n, initMap, modifiedMap, candidate, check

    initMap = [[0 for _ in range(MAX_N + 2)] for _ in range(MAX_N + 2)]
    modifiedMap = [[0 for _ in range(MAX_N + 2)] for _ in range(MAX_N + 2)]
    candidate = [[] for _ in range(MAX_HASH + 1)]
    check = [[False for _ in range(MAX_N + 2)] for _ in range(MAX_N + 2)]

    n = N
    for i in range(n):
        for j in range(n):
            modifiedMap[i + 1][j + 1] = initMap[i + 1][j + 1] = mMap[i][j]

    for length in range(2, 6):
        for i in range(1, n + 1):
            for j in range(1, n - length + 2):
                hash = 0
                for k in range(length - 1):
                    hash = hash * 10 + (initMap[i][j + k + 1] - initMap[i][j + k] + 5)
                candidate[hash].append(Candidate(i, j, True, False))

                reverseHash = 0
                for k in range(length - 1, 0, -1):
                    reverseHash = reverseHash * 10 + (initMap[i][j + k - 1] - initMap[i][j + k] + 5)
                if reverseHash != hash:
                    candidate[reverseHash].append(Candidate(i, j, True, True))

        for i in range(1, n - length + 2):
            for j in range(1, n + 1):
                hash = 0
                for k in range(length - 1):
                    hash = hash * 10 + (initMap[i + k + 1][j] - initMap[i + k][j] + 5)
                candidate[hash].append(Candidate(i, j, False, False))

                reverseHash = 0
                for k in range(length - 1, 0, -1):
                    reverseHash = reverseHash * 10 + (initMap[i + k - 1][j] - initMap[i + k][j] + 5)
                if reverseHash != hash:
                    candidate[reverseHash].append(Candidate(i, j, False, True))

def numberOfCandidate(M, mStructure):
    if M == 1:
        return n * n

    hash = 0
    for i in range(M - 1):
        hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5)

    return len(candidate[hash])

def unsubmergedArea(mMap, mSeaLevel):
    q = deque()
    for i in range(n + 2):
        for j in range(n + 2):
            if i == 0 or i == n + 1 or j == 0 or j == n + 1:
                q.append([i, j])
                check[i][j] = True
            else:
                check[i][j] = False

    while len(q) > 0:
        x, y = q[0][0], q[0][1]
        q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                if not check[nx][ny] and mMap[nx][ny] < mSeaLevel:
                    q.append([nx, ny])
                    check[nx][ny] = True

    ret = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not check[i][j]:
                ret += 1

    return ret

def maxArea(M, mStructure, mSeaLevel):
    ret = -1
    if M == 1:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                modifiedMap[i][j] = initMap[i][j] + mStructure[0]
                ret = max(ret, unsubmergedArea(modifiedMap, mSeaLevel))
                modifiedMap[i][j] = initMap[i][j]

        return ret

    hash = 0
    for i in range(M - 1):
        hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5)

    for wall in candidate[hash]:
        if wall.isHorizontal:
            height = mStructure[0] + (initMap[wall.r][wall.c + M - 1] if wall.isReverse else initMap[wall.r][wall.c])
            for i in range(M):
                modifiedMap[wall.r][wall.c + i] = height
            ret = max(ret, unsubmergedArea(modifiedMap, mSeaLevel))
            for i in range(M):
                modifiedMap[wall.r][wall.c + i] = initMap[wall.r][wall.c + i]
        else:
            height = mStructure[0] + (initMap[wall.r + M - 1][wall.c] if wall.isReverse else initMap[wall.r][wall.c])
            for i in range(M):
                modifiedMap[wall.r + i][wall.c] = height
            ret = max(ret, unsubmergedArea(modifiedMap, mSeaLevel))
            for i in range(M):
                modifiedMap[wall.r + i][wall.c] = initMap[wall.r + i][wall.c]

    return ret