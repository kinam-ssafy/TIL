'''swea4881 배열 최소 합
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    res = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # if 
    for i in range(2):
        for j in range(2):
            visited_idx = arr.index(min(arr))
            # if visited[visited_idx]
            res += min(arr)
            print(visited_idx)