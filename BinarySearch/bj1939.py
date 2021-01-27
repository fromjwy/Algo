from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]


def BFS(mid):
    q = deque([start])
    visited[start] = True

    while q:
        v1 = q.popleft()

        for v2, w in adj[v1]:
            if not visited[v2] and w >= mid:  # 중량제한을 만족하면
                visited[v2] = True
                q.append(v2)

    return visited[end]


min_w = 1000000000
max_w = 1

for _ in range(M):
    v1, v2, w = map(int, input().split())
    adj[v1].append((v2, w))
    adj[v2].append((v1, w))
    min_w = min(min_w, w)
    max_w = max(max_w, w)

start, end = map(int, input().split())

# 중량제한 이분탐색
result = 0
while min_w <= max_w:
    mid = (min_w+max_w)//2

    visited = [False for _ in range(N+1)]
    if BFS(mid):  # 목적지에 도달 가능하면
        result = mid
        min_w = mid+1
    else:
        max_w = mid-1

print(result)
