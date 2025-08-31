'''swea4881 배열 최소 합
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.'''


def dfs(i, sum):
    global min_sum
    if sum >= min_sum:
        return

    if i == N:
        min_sum = min(min_sum, sum)
        return
    
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(i + 1, sum + arr[i][j])
            visited[j] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N


    min_sum = float('inf')  #최솟값 찾기 위한 변수 선언
    dfs(0, 0)
    
    print(f"#{t} {min_sum}")
