'''swea5208 전기버스2
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 
정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.

충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.

정류장과 충전지에 대한 정보가 주어질 때, 
목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 
단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

'''
def f(i, N, e, c): # i 정류장번호, e 남은 배터리, c i-1까지 교환횟수
    global min_v
    global cnt
    cnt += 1
    if e < 0:
        return
    if i == N: # 종점에 도착
        if min_v > c:
            min_v = c
    elif min_v <= c:    # 최소 교환횟수만큼 이미 교환한 경우
        return
    else:
        f(i + 1, N, bat[i] - 1, c + 1)  # 교체
        f(i + 1, N, e - 1, c)           # 통과
 
 
T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))   # 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi
    N = bat[0]  # 정류장 수, 종점 번호
 
    min_v = N   # 최소 교환 횟수
    cnt = 0
    f(2, N, bat[1] - 1, 0)
    print(f'#{tc} {min_v}')