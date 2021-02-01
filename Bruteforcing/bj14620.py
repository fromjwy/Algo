N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]
visited = [[False]*N for _ in range(N)]
result = 10000000

# 꽃잎이 제자리,상,하,좌,우로 다 필 수 있는 지, 다른 꽃이랑 겹치는 지 확인


def check(i, j):
    for k in range(5):
        nx, ny = i+dx[k], j+dy[k]
        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or visited[nx][ny]:
            return False

    return True


def DFS(cost, cnt):
    global result
    if cnt == 3:
        result = min(result, cost)
        return

    for i in range(1, N):
        for j in range(1, N):
            if check(i, j):

                # 꽃잎을 제자리,상,하,좌,우로 피우기
                tmp = 0  # 현재 꽃을 피우는데 드는 비용
                for k in range(5):
                    nx, ny = i+dx[k], j+dy[k]
                    visited[nx][ny] = True
                    tmp += G[nx][ny]

                DFS(cost+tmp, cnt+1)
                # backtracking
                for k in range(5):
                    nx, ny = i+dx[k], j+dy[k]
                    visited[nx][ny] = False


DFS(0, 0)
print(result)
