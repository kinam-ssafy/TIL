'''swea5204 병합 정렬

알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.
'''
#나누고 정복하고 병합

def merge_sort(li):
    if len(li) == 1:
        return li
    
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]


    left_list = merge_sort(left)
    right_list = merge_sort(right)

    #병합하는 merge 함수 호출
    merge_list = merge(left_list, right_list)
    return merge_list

def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0
    
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:  #왼쪽이 더 크면
            result[l + r] = left[l]
            l += 1

        else:
            result[l + r] = right[r]
            r += 1
    while l < len(left):
        #왼쪽 리스트에 남아있는거 다 추가
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        #오른쪽 리스트에 남아있는거 다 추가
        result[l + r] = right[r]
        r += 1

    return result



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    cnt = 0

    sorted_number = merge_sort(number)
    print(f"#{tc} {sorted_number[N//2]} {cnt}")