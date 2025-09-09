'''swea5656 벽돌깨기
구술을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.

구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.

( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )

게임의 규칙은 다음과 같다.

① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.

② 벽돌은 숫자 1 ~ 9 로 표현되며,

   구술이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.

③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.

N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.

N, W, H, 그리고 벽돌들의 정보가 주어질 때,

▶ 남은 벽돌의 개수를 구하라!
'''



from collections import deque
import copy

def break_bricks(arr, start_i, start_j, H, W):
   """BFS로 벽돌 제거"""
   q = deque([(start_i, start_j, arr[start_i][start_j])])
   to_remove = set()
   to_remove.add((start_i, start_j))
   
   di = [0, 1, 0, -1]
   dj = [1, 0, -1, 0]
   
   while q:
       ci, cj, power = q.popleft()
       
       # 상하좌우로 (power-1)칸만큼 제거
       for d in range(4):
           for n in range(1, power):
               ni, nj = ci + di[d] * n, cj + dj[d] * n
               if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] > 0:
                   if (ni, nj) not in to_remove:
                       to_remove.add((ni, nj))
                       q.append((ni, nj, arr[ni][nj]))
   
   # 벽돌 제거
   for i, j in to_remove:
       arr[i][j] = 0

def apply_gravity(arr, H, W):
   """중력 처리"""
   for j in range(W):
       # 각 열에서 0이 아닌 값들을 아래로 떨어뜨리기
       temp = []
       for i in range(H):
           if arr[i][j] > 0:
               temp.append(arr[i][j])
       
       # 열 초기화 후 아래부터 채우기
       for i in range(H):
           arr[i][j] = 0
       
       for idx, val in enumerate(temp):
           arr[H - len(temp) + idx][j] = val

def find_top_brick(arr, col, H):
   """해당 열의 맨 위 벽돌 찾기"""
   for i in range(H):
       if arr[i][col] > 0:
           return i
   return -1

def count_bricks(arr, H, W):
   """남은 벽돌 개수 세기"""
   cnt = 0
   for i in range(H):
       for j in range(W):
           if arr[i][j] > 0:
               cnt += 1
   return cnt

def backtrack(arr, depth, N, W, H):
   """백트래킹으로 모든 경우의 수 시도"""
   if depth == N:
       return count_bricks(arr, H, W)
   
   min_bricks = float('inf')
   
   for col in range(W):
       # 현재 상태 저장
       temp_arr = copy.deepcopy(arr)
       
       # 해당 열의 맨 위 벽돌 찾기
       top_row = find_top_brick(temp_arr, col, H)
       
       if top_row != -1:  # 벽돌이 있으면
           # 벽돌 제거
           break_bricks(temp_arr, top_row, col, H, W)
           # 중력 처리
           apply_gravity(temp_arr, H, W)
       
       # 다음 깊이로
       result = backtrack(temp_arr, depth + 1, N, W, H)
       min_bricks = min(min_bricks, result)
   
   return min_bricks

T = int(input())

for tc in range(1, T+1):
   N, W, H = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(H)]
   
   result = backtrack(arr, 0, N, W, H)
   
   print(f"#{tc} {result}")
