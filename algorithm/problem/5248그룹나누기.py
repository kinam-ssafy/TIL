'''swea5248 그룹나누기

수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 
여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 
번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 
전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.
'''
# def find_set(x):
#     if x == parents[x]:
#         return x
    
#     parents[x] = find_set(parents)
#     return parents[x]

# def union(x, y):
#     rx = find_set(x)
#     ry = find_set(y)

#     if rx == ry: # 같은 집합이면?
#         return
    
#     if rx < ry:
#         parents[ry] = rx

#     else:
#         parents[rx] = ry
def find_set(x):
    while parents[x] != x:
        x = parents[x]
    return x

def union(x, y):
    # y의 대표원소를 x의 대표원소로 대체
    parents[find_set(y)] = find_set(x) 

    


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)

    ans = 0
    for i in range(1, N+1):
        if parents[i] == i: # 대표 원소면
            ans += 1

    print(f"#{t} {ans}")