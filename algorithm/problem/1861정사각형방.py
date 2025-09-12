'''swea1861 정사각형 방
N2개의 방이 N×N형태로 늘어서 있다.

위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 
이 숫자는 모든 방에 대해 서로 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

물론 이동하려는 방이 존재해야 하고, 
이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
'''

# 상하좌우 탐색 > 1보다 크면 이동 + 카운트 1 올라가기
# 모든 방에 대해서 다 해보기

T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr =[list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    min_num = float('inf')
    def dfs(ci, cj, start, cnt):
        global max_cnt, min_num

        if max_cnt < cnt:
            max_cnt = cnt
            min_num = start

        elif max_cnt == cnt and min_num > start:
            min_num = start


        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for dir in range(4):
            ni, nj = ci + di[dir], cj + dj[dir]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[ci][cj] == 1:
                dfs(ni, nj, start, cnt + 1)


    for a in range(N):
        for b in range(N):
            dfs(a, b, arr[a][b], 1)

    print(f"#{t} {min_num} {max_cnt}")