from collections import deque


def DFS(v):
    visited[v] = True
    print(v, end=' ')

    for dest in adj[v]:
        if not visited[dest]:
            DFS(dest)


def BFS(v):
    q = deque([v])
    visited[v] = True

    while q:
        tmp = q.popleft()
        print(tmp, end=' ')

        for dest in adj[tmp]:
            if not visited[dest]:
                visited[dest] = True
                q.append(dest)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)


# 방문가능한 정점이 여러개일 경우 정점번호가 작은 것부터 먼저 방문하기 위해
for dest in adj:
    dest.sort()

visited = [False for i in range(N+1)]
DFS(V)
print()
visited = [False for i in range(N+1)]
BFS(V)
