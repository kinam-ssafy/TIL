'''파스칼의 삼각형
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,

N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
'''


T = int(input())
for t in range(1, T+1):
    N = int(input())

    stack1 = [1]
    stack2 = []

    for i in range(N):
        if i % 2 != 0: # 홀수번째 stack1을 비우고 stack2를 채움
            stack2.append(1)
            for p in range(len(stack1)):
                stack2.append(stack1.pop())

        elif i % 2 == 0: # 짝수번째 stack2를 비우로 stack1을 채움
            stack1.append(1)
            for q in range(len(stack2)+1):



    def rec(N):
        num = 1
        if num == N:
            return

        if num == 1:


        print()
