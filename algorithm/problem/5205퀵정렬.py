'''swea5205 퀵정렬
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고,
A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    def hoare_partition(arr, left, right):
        pivot = arr[left]
        i = left + 1
        j = right

        while i <= j:
            while i <= j and arr[i] <= pivot:
                i += 1

            while i <= j and arr[j] >= pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

            
            #피벗과 j 위치 바꾸기
        arr[left], arr[j] = arr[j], arr[left]
        return j

    def quick_sort(arr, left, right):
        if left < right:
            pivot_pos = hoare_partition(arr, left, right)
            quick_sort(arr, left, pivot_pos - 1)
            quick_sort(arr, pivot_pos + 1, right)

    quick_sort(A, 0, N - 1)
    print(f"#{tc} {A[N//2]}")