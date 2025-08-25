'''swea4874 forth
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.

3 4 + .

Forth에서는 동작은 다음과 같다.

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.


Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
'''

T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input().split()))

    stack = []
    isbreak = 0
    for i in range(len(arr)):
        if len(stack) >= 2:
            if arr[i] in ['+', '-', '*', '/', '.']:

                b = int(stack.pop())
                a = int(stack.pop())

                if arr[i] == '+':
                    stack.append(a + b)

                elif arr[i] == '-':
                    stack.append(a - b)

                elif arr[i] == '*':
                    stack.append(a * b)

                elif arr[i] == '/':
                    stack.append(a // b)

                elif arr[i] == '.':
                    if len(stack) >= 2:
                        print(f"#{t} error")
                        isbreak = 1
                    break

            else:
                stack.append(int(arr[i]))
        elif isbreak == 1:
            break

        else:
            if arr[i] in ['+', '-', '*', '/']:
                print(f"#{t} error")
                isbreak = 1
                break
            stack.append(arr[i])



    if (type(stack[0]) == int) and (isbreak == 0):
        print(f"#{t} {stack[0]}")