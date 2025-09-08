'''swea5201 컨테이너 운반
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, 
A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 
옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 
컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
'''

# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())    # N개의 컨테이너, M대의 트럭
#     weight = list(map(int, input().split()))
#     truck = list(map(int, input().split()))

#     weight.sort(reverse=True)
#     truck.sort(reverse=True)

#     w_sum = 0

#     for tr in truck:
#         for w in weight:
#             if tr >= w:
#                 w_sum += w
#                 weight.pop(weight.index(w))
#                 break



#     print(f"#{t} {w_sum}")

#########################################
#반복분 하나만 쓰기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N개의 컨테이너, M대의 트럭
    W= list(map(int, input().split()))
    T = list(map(int, input().split()))

    W.sort(reverse=True)
    T.sort(reverse=True)

    i = j = 0
    total = 0
    while i < N and j < M:
        #j번 트럭이 옮길 수 있는 가장 무거운 화물 i를 찾기
        if T[j] >= W[i]:    #j번 트럭의 적재중량이 i번째 화물 무게보다 크면 옮기기
            total += W[i]
            j += 1  #화물 옮겼으면 다음 트럭으로

        i += 1  #다음화물
    
    print(f"#{tc} {total}")

