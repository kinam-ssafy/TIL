'''swea5207 이진탐색
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 
그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 
이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 B에 속한 어떤 수가 A에 들어있으면서, 
동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다. 
'''
def binary_search(arr, left, right, target, prev_dir = 0): #left, right, target
    #이전 탐색 방향 지정 prev_dir

    if left > right:    #끝나는 조건 : 못 찾은 경우
        return False
    
    mid = (left + right) // 2

    if target == arr[mid]:
        return True
    
    if target < arr[mid]:
        #왼쪽으로 이동하는 경우임
        if prev_dir == 'left':  #이전 방향이 왼쪽인데 이번에도 왼쪽으로 가면
            return False
        return binary_search(arr, left, mid-1, target, 'left')
    
    else:
        #오른쪽 탐색하는 경우
        if prev_dir == 'right': #이전방향이 오른쪽인데 또 오른쪽 탐색해야하면?
            return False
        return binary_search(arr, mid+1, right, target, 'right')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  #A와 B에 속한 정수의 개수 N M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0

    for t in B:
        #이진탐색 수행
        if binary_search(A, 0, N - 1, t):
            cnt += 1

    print(f"#{tc} {cnt}")