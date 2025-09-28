'''swea24220 경로의 수
 방향성 그래프가 있다.
 방향성 그래프와 출발, 도착 정점이 주어지면, 
 경로에 포함된 정점을 한 번만 방문해서 이동 가능한 경로가 몇 개인지 찾아보자.

* 모든 정점을 지나야 하는 것은 아니다.
* 사이클이 존재할 수 있다.

[입력]
첫 줄에 테스트케이스개수 T (1<=T<=50), 
다음 줄부터 케이스 별로 세 줄에 걸쳐 첫 줄에 마지막 정점번호 N과 간선 수 E, 다음 줄에 E개 간선의 양 끝 정점 번호(출발 도착 순), 마지막 줄에 경로를 찾기 위한 출발 정점 S와 도착정점번호G가 주어진다.
(3<=N<=20, N-1<=E<=N*(N-1)/2)
'''
def dfs(start, end):
    global ans
    if start == end:
        ans += 1

    else:
        visited[start] = 1
        for next_node in adj_list[start]:
            if not visited[next_node]:
                dfs(next_node, end)
        
        visited[start] = 0





T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    graph_info = list(map(int, input().split()))

    for i in range(E):
        a, b = graph_info[i*2], graph_info[i*2+1]
        adj_list[a].append(b)

    S, G = map(int, input().split())
    ans = 0
    dfs(S, G)

    print(f"#{t} {ans}")