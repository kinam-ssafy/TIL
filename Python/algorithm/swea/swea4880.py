'''swea4880 토너먼트 카드게임
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 
가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
 

1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 
전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
'''

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    arr =[0] + list(map(int, input().split()))
    #0번부터 n-1번 학생까지의 정보이므로 1번부터 n번까지로 늘림
    #승자의 인덱스 리턴

    def f(i, j): #i번부터 j번 사이의 승자를 리턴하는 함수
        if i == j: #한사람인 경우
            return i #그사람이 승자 
        
        else: #아니면 두 그룹으로 나눔
            left = f(i, (i+j)//2) # 왼쪽 그룹의 승자 번호
            right = f((i+j)//2 + 1, j) # 오른쪽 그룹의 승자 번호
            return winner(left, right)
        
    def winner(a, b):
        #1 가위 2 바위 3보
        #같은 카드면 번호 작은 쪽이 승자

        win = 0
        if arr[a] < arr[b] and abs(arr[a] - arr[b]) == 1:
            win = b
        
        elif arr[a] > arr[b] and abs(arr[a] - arr[b]) == 2:
            win = b

        elif arr[a] == arr[b]:
            win = a

        else:
            win = a
    
        return win



    ans = f(1, N) #1번부터 N번까지의 승자를 리턴
    print(f"#{t} {ans}")