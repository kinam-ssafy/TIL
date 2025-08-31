'''swea1222 계산기 stack2_1
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5+6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+5+6+7+"

변환된 식을 계산하면 25를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.

총 10개의 테스트 케이스가 주어진다
'''
'''
1. '3+4+5+6+7' 문자열 받기
2. 인덱스 짝수는 숫자, 홀수는 연산자
3. 계산한 결과 스택에 넣기
4. 스택에서 빼서 계산하고 다시 넣기
'''


T = 10
for t in range(1, T+1):
    length = int(input()) #문자열의 길이
    calc = input()
    number = []
    operator = []
    stack = []

    for i in range(length):
        if i % 2 == 0:
            number.append(int(calc[i]))
        else:
            operator.append(calc[i])
    stack.append(number[0])
    idx = 0
    while idx < len(operator):
        num = stack.pop()

        if operator[idx] == '+':
            num += number[idx+1]
            stack.append(num)
        idx += 1

    print(f"#{t} {stack[-1]}")
