'''swea4871 그래프 경로
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
'''

# T = int(input())
# for t in range(1, T+1):
#     V, E = map(int, input().split())
#     # 이제 E개의 줄에 걸쳐 출발, 도착 노드로 간선 정보 주어짐
#     arr = [[] for _ in range(V + 1)]
#     for _ in range(E):
#         u, v = map(int, input().split())
#         arr[u].append(v)

#     S, G = map(int, input().split())

#     visited = [False] * (V + 1)

#     def dfs(arr, visited, start, end):
#         visited[start] = True
#         if start == end:
#             return True

#         for neighbor in arr[start]:
#             if not visited[neighbor]:
#                 if dfs(arr, visited, neighbor, end):
#                     return True
#         return False

#     if dfs(arr, visited, S, G):
#         result = 1
#     else:
#         result = 0

#     print(f"#{t} {result}")



def dfs(s, g):
    visited[s] = 1

    while stack:
        t = stack.pop()
        
        for i in t:
            if i == g:
                return 1 

            elif visited[i] == 0:
                stack.append(graph[i])
                visited[i] = 1

    return 0



T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())    #V 노드 개수, E간선 정보 개수
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for i in range(E):
        p, c = map(int, input().split())
        graph[p].append(c)
    # print(graph)
    S, G = map(int, input().split())

    start = graph[S]
    stack = [start]
    
    result = dfs(S, G)
    print(f"#{t} {result}")
