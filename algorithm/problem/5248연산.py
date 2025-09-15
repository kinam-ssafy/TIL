'''swea5248 연산
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 
연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.
1<=N, M<=1,000,000
'''
from collections import deque


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001


    def go_next(current):
        next_list = []
        if 1 <= current + 1 <= 1000000:
            next_list.append(current + 1)

        if 1 <= current - 1 <= 1000000:
            next_list.append(current - 1)

        if 1 <= current * 2 <= 1000000:
            next_list.append(current * 2)

        if 1 <= current - 10 <= 1000000:
            next_list.append(current - 10)
        
        return next_list

    def bfs(N, M):
        q = deque([[N, 0]]) #시작점, count 연산 횟수
        visited[N] = 1


        while q:
            cur, cnt = q.popleft()
            next_list = go_next(cur)

            if cur == M:
                return cnt

            for next_num in next_list:
                if not visited[next_num]:
                    visited[next_num] = 1
                    q.append([next_num, cnt + 1])

    ans = bfs(N, M)
    print(f"#{t} {ans}")