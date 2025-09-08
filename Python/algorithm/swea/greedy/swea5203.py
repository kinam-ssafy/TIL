'''swea5203 베이비진 게임 D2
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 
6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 
만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 
플레이어 1은 9, 5, 5, 1, 4, 2카드를, 
플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.

'''
# 입력받은 배열의 홀수 인덱스는 플레이어 2 짝수 인덱스는 플레이어 1로 나눔
# run or triplet이 먼저 되면 승리



# def run_or_triplet(arr):
#     #카운트 배열 만들기
#     # 0~9까지의 숫자를 셀 것
#     count = [0] * 10

#     for card in arr:
#         count[card] += 1
    


#     #triplet 체크
#     for i in range(10):
#         if count[i] >= 3:   #같은숫자 3개
#             return True
        
#     #run 체크
#     for i in range(8):
#         if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1:   #연속된숫자 3개
#             return True
        
#     return False
    

# T = int(input())

# for t in range(1, T+1):
    
#     cards = list(map(int, input().split()))
#     p1 = []
#     p2 = []
#     isbreak = 0
#     for i in range(len(cards)):
#         if i % 2 == 0:  #인덱스 0은 2로 나눠도 나머지 0이므로 p1부터 시작
#             p1.append(cards[i])
#             #p1의 카드가 3장 이상이면 run or triplet 실시
#             if len(p1) >= 3 and run_or_triplet(p1):    
#                 print(f"#{t} {1}")
#                 isbreak = 1
#                 break

#         elif i % 2 == 1:    #인덱스 1, 3, 5, 7 .... 은 p2에게
#             p2.append(cards[i])

#             if len(p2) >= 3 and run_or_triplet(p2):
#                 print(f"#{t} {2}")
#                 isbreak = 1
#                 break
    
#     if isbreak == 0:
#         print(f"#{t} 0")
    


##############################################

#이전 코드는 카운트배열을 매번 만들어야해서 개선

# def run_or_triplet(arr):
#     #triplet 체크
#     for i in range(10):
#         if arr[i] >= 3:   #같은숫자 3개
#             return True
        
#     #run 체크
#     for i in range(8):
#         if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:   #연속된숫자 3개
#             return True
        
#     return False

# T = int(input())

# for t in range(1, T+1):
    
#     cards = list(map(int, input().split()))
#     p1 = [0] * 10
#     p2 = [0] * 10
#     isbreak = 0
#     for i in range(len(cards)):
#         if i % 2 == 0:  #인덱스 0은 2로 나눠도 나머지 0이므로 p1부터 시작
#             p1[cards[i]] += 1
#             #p1의 카드가 3장 이상이면 run or triplet 실시
#             if sum(p1) >= 3 and run_or_triplet(p1):    
#                 print(f"#{t} {1}")
#                 isbreak = 1
#                 break

#         elif i % 2 == 1:    #인덱스 1, 3, 5, 7 .... 은 p2에게
#             p2[cards[i]] += 1

#             if sum(p2) >= 3 and run_or_triplet(p2):
#                 print(f"#{t} {2}")
#                 isbreak = 1
#                 break
    
#     if isbreak == 0:
#         print(f"#{t} 0")

####################################################
#한 번 더 개선

def run_or_triplet(arr):
    #triplet or run 체크
    for i in range(10):
        if arr[i] >= 3 or (arr[i] and arr[i+1] and arr[i+2]):
            return True
        
    return False

T = int(input())

for t in range(1, T+1):
    
    cards = list(map(int, input().split()))
    #카운트 배열 0~9까지 [0] * 10
    #run ot triplet 에서 range(10)에 대해 arr[i+2]까지 탐색해야해서 [0] * 10 을 [0] * 12로 늘려줌
    p1 = [0] * 12
    p2 = [0] * 12
    winner = 0
    for i in range(len(cards)):
        if i % 2 == 0:  #인덱스 0은 2로 나눠도 나머지 0이므로 p1부터 시작
            p1[cards[i]] += 1
            #p1의 카드가 3장 이상이면 run or triplet 실시
            if sum(p1) >= 3 and run_or_triplet(p1):    
                winner = 1
                break

        elif i % 2 == 1:    #인덱스 1, 3, 5, 7 .... 은 p2에게
            p2[cards[i]] += 1   

            if sum(p2) >= 3 and run_or_triplet(p2):
                winner = 2
                break

    print(f"#{t} {winner}")