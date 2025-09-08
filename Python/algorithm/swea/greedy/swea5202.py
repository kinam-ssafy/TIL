'''swea5202 화물 도크
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.

0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []

    for i in range(N):
        start, end = map(int, input().split())
        arr.append([start, end])

    #끝나는시간, 시작시간 순으로 정렬
    arr.sort(key = lambda x : (x[1], x[0]))

    start = 0
    end = 0
    cnt = 0

    #이전 회의의 끝나는시간이 현재회의의 시작시간 이하여야 회의 시작가능
    for s, e in arr:
        if end <= s:
            cnt += 1
            end = e

    print(f"#{t} {cnt}")