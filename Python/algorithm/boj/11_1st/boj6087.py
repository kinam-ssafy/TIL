'''boj6087 - 레이저 통신
문제
크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 
지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.

'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 
레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.

레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.

아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.

7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
입력
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)

둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.

.: 빈 칸
*: 벽
C: 레이저로 연결해야 하는 칸
'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.

출력
첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.
'''

import sys
from collections import deque
input = sys.stdin.readline



W, H = map(int, input().split())

minimap = [list(map(str, input().strip())) for _ in range(H)]
# print(minimap)

turn = 10000

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 시작점 찾기
points = []
for i in range(H):
    for j in range(W):
        if minimap[i][j] == 'C':
            points.append((i, j))

start = points[0]
end = points[1]

# mirror[i][j][d] = i, j에 d방향으로 도착했을 때의 최소 거울 수
mirror = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]

q = deque()

for d in range(4):
    q.append((start[0], start[1], d, 0)) # (i, j, 방향, 거울 수)
    mirror[start[0]][start[1]][d] = 0

ans = 100000

while q:
    ci, cj, cur_dir, mirrors = q.popleft()

    #도착점
    if (ci, cj) == end:
        ans = min(ans, mirrors)
        continue
    
    # 현재 꺼낸 mirrors가 이전보다 더 크면 거울로 방문한 경우 
    if mirrors > mirror[ci][cj][cur_dir]:
        continue # 경로 버림
    
    for next_dir in range(4):
        ni, nj = ci + di[next_dir], cj + dj[next_dir]

        if not(0 <= ni < H and 0 <= nj < W): # 범위체크
            continue
        
        if minimap[ni][nj] == '*': # 벽이면?
            continue
        
        if cur_dir == next_dir: # 현재방향이랑 다음 방향 같으면 거울 수 같음
            new_mirrors = mirrors
        
        elif cur_dir != next_dir: # 방향 다르면 거울 수 늘어남
            new_mirrors = mirrors + 1

        if new_mirrors < mirror[ni][nj][next_dir]:
            mirror[ni][nj][next_dir] = new_mirrors

            if cur_dir == next_dir: # 같은 방향이면 큐의 앞에 추가 
                q.appendleft((ni, nj, next_dir, new_mirrors))
            
            else: # 아니면 뒤로 추가
                q.append((ni, nj, next_dir, new_mirrors))

print(ans)
