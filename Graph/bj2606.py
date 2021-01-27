from collections import deque

com = int(input())
N = int(input())
adj = [[] for _ in range(com+1)]
visited = [False for _ in range(com+1)]
cnt = 0

for _ in range(N):
    c1, c2 = map(int, input().split())
    adj[c1].append(c2)
    adj[c2].append(c1)

'''
def DFS(v):
    global cnt
    cnt += 1
    visited[v] = True
    for next in adj[v]:
        if not visited[next]:
            visited[next] = True
            DFS(next)

DFS(1)
print(cnt-1)
'''


def BFS(v):
    global cnt
    q = deque([v])
    visited[v] = True

    while q:
        cnt += 1
        tmp = q.popleft()

        for next in adj[tmp]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


BFS(1)
print(cnt-1)
