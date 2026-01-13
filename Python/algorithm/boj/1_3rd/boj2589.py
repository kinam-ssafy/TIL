'''
boj2589 - 보물섬
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.



예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.



보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.


첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.
'''

"""
1. 최단 거리
2. 가장 긴 시간
3. 같은 곳을 두 번 이상 지나가거나 멀리 돌아가기 x

DFS 백트래킹? BFS?

시간 초과 >> 육지가 이어져있는곳마다 dfs를 시행하니 시간이 오래걸림
한 육지 세션에 대해서 임의의 육지에 dfs를 두 번 수행하면 최장시간 구할 수 있을 것 >>> 트리가 아니라서 최단거리 보장 x, 사이클 존재
나머지는 방문처리해서 dfs 수행 줄여보기

그냥 bfs가 최단거리 보장하니까 bfs수행하기

문제 : 각 지점에 대해서 모두 BFS를 수행하기로 했는데 한 점에 대해서 BFS끝나면 visited배열 초기화 해줘야함
>> BFS의 시작점을 이중포문으로 arr[i][j] == 'L'이면 한 리스트에 모두 담아서 다 BFS를 수행했었는데
BFS수행 시작점 하나 찾으면 바로 그 지점에서 BFS를 수행하고 끝나면 visited 배열을 초기화 하는 방식으로 진행함
"""

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# N, M = map(int, input().split())

# arr = [list(input().strip()) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# start = []

# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'L':
#             start.append((i, j))

# ans = 0

# dfsi = 0
# dfsj = 0

# def dfs(si, sj, dist):
#     global ans, dfsi, dfsj
#     if ans < dist:
#         ans = dist
#         dfsi = si
#         dfsj = sj

#     for d in range(4):
#         ni, nj = si + di[d], sj + dj[d]
#         if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
#             visited[ni][nj] = 1
#             dfs(ni, nj, dist + 1)
#             visited[ni][nj] = 0

# def ddfs(si, sj, dist):
#     global ans
#     if ans < dist:
#         ans = dist

#     for d in range(4):
#         ni, nj = si + di[d], sj + dj[d]
#         if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
#             visited[ni][nj] = 1
#             ddfs(ni, nj, dist + 1)


# for i in range(len(start)):
#     si, sj = start[i]
#     if visited[si][sj] == 0:
#         visited[si][sj] = 1
#         dfs(si, sj, 0)
#         visited[si][sj] = 0
#         ddfs(dfsi, dfsj, 0)

# print(ans)

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

q = deque([])
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            q.append((i, j, 0))
            visited = [[0] * M for _ in range(N)]

            while q:
                ci, cj, dist = q.popleft()

                if not visited[ci][cj]:
                    visited[ci][cj] = 1

                if ans < dist:
                    ans = dist

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 'L':
                        visited[ni][nj] = 1
                        q.append((ni, nj, dist + 1))

print(ans)