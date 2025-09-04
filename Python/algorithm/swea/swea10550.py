'''swea10550 baby-gin(완전검색 그리디)

1부터 9로 구성된 6개의 숫자를 읽어 베이비진을 판단하는 프로그램을 만드시오
- 3장의 카드가 연속적인 번호 : run
- 3장의 카드가 동일한 번호 : triplet
- 6장의 카드가 run과 triplet으로 구성된 경우 : baby-gin
입력
첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 6자리 수가 주어진다.

출력
#과 테스트케이스 번호, 빈 칸에 이어 Baby Gin 또는 Lose를 출력한다.
'''

def is_babygin(n):
    #run or triplet 으로만 이루어져있으면 baby gin
    if n == 3:
        if is_tri_or_run(path):
            #리스트에 먼저 들어온 3개가 tri or run이면
            #나머지 숫자 3개를 나머지 리스트로 만듦
            skajwl = [num[i] for i in range(len(num)) if not visited[i]]
            #나머지 리스트에 대해서도 tri or run인지 
            return is_tri_or_run(skajwl)
        
        else:
            return False
            
    if n == 6:
        return True

    for i in range(len(num)):
        if not visited[i]:
            visited[i] = 1
            path.append(num[i])
            if is_babygin(n+1):
                return True
            path.pop()
            visited[i] = 0


    return False

def is_tri_or_run(arr): # triplet인지 run인지 판단
    arr = arr.copy()
    arr.sort()
    if arr[0] == arr[1] == arr[2]: return True
    if arr[0] == arr[1]-1 == arr[2]-2: return True

    return False


T = int(input())
for t in range(1, T+1):
    num = list(map(int, input()))
    path = []
    visited = [0]*6

    result = is_babygin(0)
    if result:
        print(f"#{t} Baby Gin")

    else:
        print(f"#{t} Lose")
