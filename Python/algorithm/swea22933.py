'''swea22933 IM대비
싸피부분배열이란 NxN크기의 배열 내부의 직사각형 영역에서 왼쪽 위와 오른쪽 아래
모서리에 위치한 원소의 값이 같고, 그 중 면적이 가장 넓은 부분 배열을 가리킨다.

2차원 배열이 주어지면 여기에서 싸피부분배열의 개수를 찾아 출력하라.
만약 모든 원소의 숫자가 다르면 싸피부분배열의 면적은 1이고, 개수는 NxN개가 된다.
'''

#완전 탐색.. 각 인덱스에 대하여 같은 값을 찾고, 해당 인덱스 저장
#넓이 구해서 맥스값 갱신

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(f"arr : {arr}")

    max_area = 1
    cnt = 1
    for i in range(N):
        for j in range(N):#현재 위치
            current = arr[i][j]
            # print(f"current : {current}")
            for p in range(i, N):
                for q in range(j, N):#비교할 위치
                    if i == p and q == j:
                        continue
                    #현재값과 비교값이 같은 인덱스를 가리키지 않고 값이 같다면
                    # print(f"arr[p][q]: {arr[p][q]}")
                    if arr[i][j] == arr[p][q]:
                        area = abs(p-i+1) * abs(q-j+1) #면적을 구해줌
                        if max_area < area:
                            max_area = area # 최대면적 갱신
                            cnt = 1 #카운트값 갱신
                            # print(f"max area : {max_area}")

                        elif max_area == area: #최대면적 같으면 카운트 올라감
                            cnt += 1
                            # print(f"cnt : {cnt}")
    if max_area == 1:
        cnt = N * N


    print(f"#{t} {cnt}")


