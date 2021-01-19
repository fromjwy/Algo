R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    global result
    q = [(x, y, board[x][y])]

    while q:
        x, y, path = q.pop()
        result = max(result, len(path))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # promising 체크
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in path):
                q.append((nx, ny, path+board[nx][ny]))


result = 0
BFS(0, 0)

print(result)
