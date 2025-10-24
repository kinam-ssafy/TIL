'''boj9935 - 문자열 폭발

상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
'''
# replace로 A문자열에서 B문자열 제거하기
# 시간 복잡도 초과

# import sys
# input = sys.stdin.readline

# str1 = input().strip() # 문자열
# explosion = input().strip() # 폭발 문자열
# ans = str1.replace(explosion, '')

# while ans != str1:
#     str1 = ans
#     ans = str1.replace(explosion, '')
#     if ans == '':
#         print('FRULA')
#         exit()
# print(ans)

#############################################

# stack으로 구현해보기
# 문자 하나하나 넣다가 폭발 문자열 있으면 폭발 문자열 길이만큼 pop해주기

import sys
input = sys.stdin.readline

str1 = input().strip() # 문자열
explosion = input().strip() # 폭발 문자열
n = len(explosion)

stack = []

for char in str1:
    stack.append(char)
    if len(stack) >= n: # 스택에 폭발 문자열 길이만큼 문자가 들어갔으면
        if ''.join(stack[len(stack)-n:]) == explosion: # 스택의 마지막 부분 합쳐서 폭발 문자열이랑 같으면
            for _ in range(n): # 폭발 문자열 길이만큼 pop하기
                stack.pop() 

if not stack:
    print('FRULA')

else:
    print(''.join(stack))