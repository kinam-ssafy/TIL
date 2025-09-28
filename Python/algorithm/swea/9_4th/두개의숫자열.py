'''swea 1959 두 개의 숫자열

N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.

단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

위 예제의 정답은 아래와 같이 30 이 된다.
'''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    current = 0
    ans = 0

    if N > M:
        for i in range(N-M+1):
            current = 0
            for j in range(M):
                current += (A[i+j] * B[j])
            
            ans = max(current, ans)
            
    elif N < M:
        for i in range(M-N+1):
            current = 0
            for j in range(N):
                current += (B[i+j] * A[j])

            ans = max(current, ans)

    else:
        for i in range(N):
            current += A[i] * B[i]

    print(f"#{t} {ans}")