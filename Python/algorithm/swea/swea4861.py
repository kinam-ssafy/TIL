'''swea4861 회문
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
'''

#가로로 회문찾기 1행에 대해서 회문 검사 가능
#세로로 회문찾기 1열에 대해서 회문 검사 가능

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    isbreak = 0
    print(f"#{t} ", end='')

    for i in range(N):#각 행에 대하여
        for j in range(N-M+1):
            mini_str = arr[i][j:j+M+1]
            if mini_str == mini_str[::-1]:
                print(''.join(mini_str))
                isbreak = 1
                break
        if isbreak == 1:
            break

        for a in range(N-M+1): #열 회문 검사
            mini_str = []
            for m in range(M):
                mini_str += arr[a+m][i] # 각 열에 대한 값을 하나씩 넣어줌
            if mini_str == mini_str[::-1]:
                print(''.join(mini_str))
                break












