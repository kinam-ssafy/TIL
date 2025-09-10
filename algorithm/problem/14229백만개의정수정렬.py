'''swea14229 백만개의 정수 정렬
공백으로 구분된 백만개의 정수가 주어진다.
오름차순으로 정렬한 후 배열 A에 저장하고 A[500000]을 출력하라.
'''

# 퀵 정렬 해보기
import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')


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

quick_sort(A, 0, len(A) - 1)
print(A[500000])

