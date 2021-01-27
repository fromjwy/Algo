from collections import deque


def BFS(N):
    q = deque([N])

    while q:
        now = q.popleft()
        if now == K:
            return time[now]

        for next in (now-1, now+1, now*2):
            if 0 <= next <= Max and time[next] == 0:
                time[next] = time[now] + 1
                q.append(next)


N, K = map(int, input().split())
Max = 100001
time = [0 for _ in range(Max+1)]

print(BFS(N))
