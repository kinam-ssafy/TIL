T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    L = 1               # 정답이 존재하는 가능성이 있는 왼쪽 끝
    R = 10000000000     # 정답이 존재하는 가능성이 있는 오른쪽 끝
    res = 0             # 내가 찾은 최고의 정답

    while L <= R:
        mid = (L + R) // 2              # mid 단 삼각형을 만들 예정
        value = mid * (mid + 1) // 2    # mid 단 삼각형에 필요한 양초 개수

        if N >= value:      # * 가능한 케이스
            res = mid       # 정답을 갱신
            L = mid + 1     # 오른쪽 절반에 대해 추가 탐색
        else:               # * 불가능한 케이스
            R = mid - 1     # 왼쪽 절반에 대해 추가 탐색

    value = res * (res + 1) // 2

    if N != value:
        res = -1

    print(f'#{test_case} {res}')