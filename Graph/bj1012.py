from collections import deque

tc = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
M, N, K = 0, 0, 0


def BFS(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    Map[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if Map[nx][ny] == 0 or visited[nx][ny] == 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = 1
            Map[nx][ny] = 0


for _ in range(tc):
    M, N, K = map(int, input().split())
    Map = [[0]*(M+1) for _ in range(N+1)]
    visited = [[0]*(M+1) for _ in range(N+1)]

    for _ in range(K):
        y, x = map(int, input().split())
        Map[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0 or visited[i][j] == 1:
                continue

            BFS(i, j)
            cnt += 1

    print(cnt)
