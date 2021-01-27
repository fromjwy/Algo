from collections import deque


def BFS(v):
    visited = [False for _ in range(N+1)]
    q = deque([v])
    visited[v] = True
    cnt = 1

    while q:
        tmp = q.popleft()

        for next in adj[tmp]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1

    return cnt


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[B].append(A)

result = []

for i in range(1, N+1):
    result.append(BFS(i))

for idx, cnt in enumerate(result):
    if cnt == max(result):
        print(idx+1, end=' ')
