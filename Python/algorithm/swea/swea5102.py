'''swea5102 노드의 거리
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''
def bfs(s, g, v):  #시작점, 끝점, 노드 개수
    visited = [0] * (v+1)
    q = [s]
    visited[s] = 1

    while q:
        t = q.pop(0)

        if t == g: # 도착노드면
            return visited[t] - 1
        
        for w in arr[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    

    for i in range(E):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)  #방향 표시가 없음

    S, G = map(int, input().split())

    result = bfs(S, G, V)
    print(f"#{t} {result}")