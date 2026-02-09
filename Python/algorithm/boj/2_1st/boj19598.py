"""boj19598 - 최소 회의실 개수

서준이는 아빠로부터 N개의 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라는 미션을 받았다. 
각 회의는 시작 시간과 끝나는 시간이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 
단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작 시간은 끝나는 시간보다 항상 작다. N이 너무 커서 괴로워 하는 우리 서준이를 도와주자.

첫째 줄에 배열의 크기 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N+1 줄까지 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 231−1보다 작거나 같은 자연수 또는 0이다.

예제 입력 1 
3
0 40
15 30
5 10
예제 출력 1 
2

0~40 
5~10, 15~30 
회의실 두개

0 40
5 10
15 30
20 40 이면?

0 40
5 10 15 30
20 40  
3개?

1. (0, 40) -> [40]
2. (5, 10) 시작시간이 이전 회의의 끝나는 시간보다 일찍임. 5 < 40 [40, 10] 회의 2개
3. (15, 30) 15 > 10 ... 10을 빼고 30 넣기 [40, 30]
4. (20, 40) 20 < 30 ... [40, 30, 40]

[(0, 40), (5, 10), (15, 30)]
for i in range(len(arr)):
    arr[i][0]

"""

# 시작 시간 순으로 정렬,

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
meetings = []

arr.sort(key=lambda x:(x[0], x[1]))

for i in range(len(arr)):
    if not meetings:
        heappush(meetings, arr[i][1]) #끝나는 시간을 넣어줌

    elif arr[i][0] >= meetings[0]:
        heappop(meetings)
        heappush(meetings, arr[i][1])   

    elif arr[i][0] < meetings[0]:
        heappush(meetings, arr[i][1])

print(len(meetings))


