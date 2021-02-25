import copy
from collections import deque

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
#visited = [[0]*M for _ in range(N)]
# 0 빈칸 1 벽 2 바이러스

# 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

virusList = []
res = 0
cnt = 0

# 바이러스 퍼트리기

'''
def spreadVirus(x, y, tmp):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if tmp[nx][ny] == 0:
            tmp[nx][ny] = 2
            spreadVirus(nx, ny, tmp)
'''
def spreadVirus(x, y, tmp):
    q = deque([(x,y)])

    while q:
        xx,yy = q.popleft()
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx,ny))

# 벽 3개 세우기
def wall(start, cnt):
    global res
    if cnt == 3:
        # 바이러스 퍼트리기
        tmp = copy.deepcopy(Map)
        for num in range(len(virusList)):
            r, c = virusList[num]
            spreadVirus(r, c, tmp)
        # 안전영역 크기 최대크기 갱신
        res = max(res, sum([x.count(0) for x in tmp]))
        return

    # 벽 세우기
    for i in range(start, N*M):  # 2차원 배열에서 조합
        r = i // M
        c = i % M
        if Map[r][c] == 0:
            Map[r][c] = 1
            wall(i+1, cnt+1)
            Map[r][c] = 0


# 바이러스 위치 찾기
for x in range(N):
    for y in range(M):
        if Map[x][y] == 2:
            virusList.append((x, y))

wall(0, 0)
print(res)
