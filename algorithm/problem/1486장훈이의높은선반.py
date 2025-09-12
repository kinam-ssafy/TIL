'''swea1486 장훈이의 높은 선반

장훈이는 서점을 운영하고 있다.

서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에, 
선반 위의 물건을 자유롭게 사용할 수 있다.


어느 날 장훈이는 자리를 비웠고, 이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.

각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.
점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.

탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.

탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 
탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.
'''

# 점원의 키를 합쳐서 탑의 높이와의 차이가 가장 작은 것을 출력

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (N + 1)
    min_sum = float('inf')

    def dfs(idx, sum):
        global min_sum

        if sum >= B:
            min_sum = min(min_sum, sum)
            return
        
        if idx >= N:
            return
        
        dfs(idx + 1, sum)
        dfs(idx + 1, sum + arr[idx])


    dfs(0, 0)    
    print(f"#{t} {min_sum-B}")