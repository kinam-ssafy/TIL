'''boj16724
문제
피리 부는 사나이 성우는 오늘도 피리를 분다.

성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다. 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해 특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다. 하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다. 

성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.

두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.

지도 밖으로 나가는 방향의 입력은 주어지지 않는다.

출력
첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.
'''

# 회원들이 어느 구역에 있더라도 Safe zone에 들어갈 수 있어야 함
# case 1: 사람들이 마지막으로 모이는 장소는 그 전 방향과 반대방향이었음 ex) R L, U D 
# case 2: 다음 방향이 갈 곳이 없으면 모이는 장소 ex) 방향이 R인데 range에서 벗어나는 경우

# case 3: 순환이 되는 싸이클인 경우 ex) 상하좌우로 계속 순환 << 어떻게 확인하지
# 그냥 싸이클만 확인해도 다 확인 가능할 것 같음 >> union find가 싸이클 확인하기 좋을 것 같다
# 2차원 배열에서 union find 어떻게 구현하지?


# N, M = map(int, input().split())

# arr = [list(input()) for _ in range(N)]

# di = [0, 1]
# dj = [1, 0]

# ans = 0

# for i in range(N):
#     for j in range(M):
#         for d in range(2):
#             ni, nj = i + di[d], j + dj[d]
#             if 0 <= ni < N and 0 <= nj < M: 
#                 if d == 0: # 좌우 case 1
#                     if arr[i][j] == 'R': #현재 위치가 오른쪽으로 가라는 표식일 때 
#                         if arr[ni][nj] == 'L':
#                             ans += 1
#                         elif nj >= M: # 오른쪽에 있는 좌표가 오른쪽에 갈 곳이 없는 경우(배열의 범위에서 벗어난 경우) case2
#                             ans += 1
#                     elif arr[i][j] == 'L': # 현재 위치가 왼쪽으로 가라는 표식일 때
#                         if arr[ni][nj] == 'R':
#                             ans += 1
#                         elif nj < 0: # 왼쪽에 있는 좌표가 배열의 범위에서 벗어난 경우\
#                             ans += 1
#                 elif d == 1: # 상하 case 1           
#                     if arr[i][j] == 'U': # 현재 위치가 위로 가라는 표식
#                         if arr[ni][nj] == 'D':
#                             ans += 1
#                         elif ni < 0:
#                             ans += 1
#                     elif arr[i][j] == 'D': # 현재위치가 아래로 가라는 표식
#                         if arr[ni][nj] == 'U':
#                             ans += 1
#                         elif ni >= N:
#                             ans += 1

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# visited = [[0] * M for _ in range(N)]    

# def dfs(si, sj):
#     visited[si][sj] = 1
#     for d in range(4):
#         ni, nj = si + di[d], sj + dj[d]
#         if 0 <= ni < N and 0 <= nj < M:
#             if arr[si][sj] == 'R' and visited[si][sj+1] == 0:
#                 dfs(si, sj + 1)
#             elif arr[si][sj] == 'L' and visited[si][sj-1] == 0:
#                 dfs(si, sj - 1)
#             elif arr[si][sj] == 'U' and visited[si-1][sj] == 0:
#                 dfs(si - 1, sj)   
#             elif arr[si][sj] == 'D' and visited[si+1][sj] == 0:
#                 dfs(si + 1, sj)   


            
# dfs(0, 0)

# print(ans)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 2. 부모 배열 초기화 (2차원을 1차원으로 펼침)
parent = [i for i in range(N * M)]

# 3. Find 함수: 대표 노드 찾기
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

# 4. Union 함수: 두 노드를 하나의 그룹으로 합치기
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_a] = root_b


for i in range(N):
    for j in range(M):
        curr = i * M + j # 현재 위치의 1차원 인덱스
        
        # 방향에 따른 다음 좌표 계산
        if arr[i][j] == 'R':
            ni, nj = i, j + 1
        elif arr[i][j] == 'L':
            ni, nj = i, j - 1
        elif arr[i][j] == 'U':
            ni, nj = i - 1, j
        elif arr[i][j] == 'D':
            ni, nj = i + 1, j
            
        next = ni * M + nj # 다음 위치의 1차원 인덱스
        union(curr, next) # 현재 칸과 다음 칸을 한 그룹으로 묶음

#자기 자신이 부모인 노드의 개수 = 그룹(사이클)의 개수
ans = 0
for i in range(N * M):
    if parent[i] == i:
        ans += 1

print(ans)