'''swea5209 최소생산비용

A사는 여러 곳에 공장을 갖고 있다. 
봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

'''
def dfs(row, sum):
    global min_sum

    if min_sum < sum:
        return
    
    if row == N:
        min_sum = min(min_sum, sum)
        return
    
    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            dfs(row + 1, sum + arr[row][col])
            visited[col] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = float('inf')
    
    dfs(0, 0)

    

    print(f"#{t} {min_sum}")