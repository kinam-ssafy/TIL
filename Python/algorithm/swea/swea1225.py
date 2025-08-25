'''swea1225 암호 생성기
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
'''
from collections import deque

for t in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    arr = deque(arr)
    i = 1
    while 0 not in arr:
        num = arr.popleft()
        num -= i
        if num < 0:
            num = 0
        arr.append(num)
        i += 1
        if i > 5:
            i = 1

    print(f"#{t} ", *list(arr))