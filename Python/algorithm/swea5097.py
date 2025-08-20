'''swea5097 회전 queue
N개의 숫자로 이루어진 수열이 주어진다. 
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
'''
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    
    #수식으로 풀기
    # res = M % len(queue)
    # print(f"#{t} {queue[res]}")

    #queue로 풀기
    # q = deque(queue)

    # for i in range(M):
    #     rear = q.popleft()
    #     q.append(rear)

    # result = q[0]
    # print(f"#{t} {result}")

    #원형큐
    q = deque(queue)
    q.rotate(-M)

    print(f"#{t} {q[0]}")
