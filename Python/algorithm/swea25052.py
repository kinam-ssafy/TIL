'''swea25052 등산로 IM대비
높이가 서로 다른 NxN 크기의 영역에서 등산로를 만들고자 한다.

등산로를 만드는 규칙은 다음과 같다.

- 출발은 어디서든 가능하다.
- 상하좌우로 인접한 영역 중 더 낮은 영역으로만 이동할 수 있다.
- 더 낮은 영역이 여러 개인 경우 그 중 가장 낮은 곳으로 이동해야 한다.
- 만약 더 낮은 인접 영역이 없으면 더 이상 이동할 수 없다.
- 주어진 지도에서 만들 수 있는 가장 긴 등산로의 길이는 얼마인가?
가장 긴 등산로는 여러 개가 만들어질 수 있다.
'''

# 1. 완전탐색 >> 모든 배열 순회하기
# 2. 델타 이용하여 주변 상하좌우 인덱스 중 가장 낮은 수로 가기
# 3. 이동한만큼 카운트 증가

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_cnt = 1 #등산로의 최대 길이

    for i in range(N):
        for j in range(N):
            current_min = arr[i][j] #처음 위치의 값을 최소값으로 할당
            current_i = i
            current_j = j
            cnt = 1
            while True:
                next_i = 0
                next_j = 0
                for ni, nj in list(zip(di, dj)): #주변에서 가장 낮은곳 찾기
                    if 0 <= current_i+ni < N and 0 <= current_j+nj < N:
                        if current_min > arr[current_i+ni][current_j+nj]:
                            current_min = arr[current_i+ni][current_j+nj]
                            next_i, next_j = ni, nj

                if next_i == 0 and next_j == 0: #가장낮은곳이 없으면 끝
                    break

                current_i += next_i #주변에서 가장 낮은 곳으로 인덱스 이동
                current_j += next_j
                cnt += 1 #등산로의 길이 1증가

            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{t} {max_cnt}")


