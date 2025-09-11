'''swea1865 동철이의 일 분배

동철이가 차린 전자회사에는 N명의 직원이 있다.

그런데 어느 날 해야할 일이 N개가 생겼다.

동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, 
i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.

여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.

직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.

우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.

'''
def dfs(row, sum):
    global max_sum

    if row == N:
        # print(max_sum, sum)
        max_sum = max(max_sum, sum)
        return
    
    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            dfs(row + 1, sum * arr[row][col])
            visited[col] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    visited = [0] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    
    dfs(0, 1)
    print(f"#{t} {max_sum/100**(N-1)}")
    