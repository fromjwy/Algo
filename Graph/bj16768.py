from collections import deque
import sys
sys.setrecursionlimit(1000)

N, K = map(int, input().split())
Map = [list(input()) for _ in range(N)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def countMooyo(x, y, val):
    cnt = 1
    ck[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= 10:
            continue

        if ck[nx][ny] or Map[nx][ny] != val:
            continue

        cnt += countMooyo(nx, ny, val)
    return cnt


def deleteMooyo(x, y, val):
    Map[x][y] = '0'
    ck2[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= 10:
            continue

        if ck2[nx][ny] or Map[nx][ny] != val:
            continue

        deleteMooyo(nx, ny, val)


def Down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if Map[j][i] != '0':
                tmp.append(Map[j][i])
        for j in range(N-len(tmp)):
            Map[j][i] = '0'
        for j in range(N-len(tmp), N):
            Map[j][i] = tmp[j-(N-len(tmp))]


mooyo = 0

while True:
    flag = False
    ck = [[False]*10 for _ in range(N)]
    ck2 = [[False]*10 for _ in range(N)]

    for i in range(N):
        for j in range(10):
            if Map[i][j] == '0' or ck[i][j]:
                continue

            val = Map[i][j]
            mooyo = countMooyo(i, j, val)  # 그룹의 갯수 세기

            if mooyo >= K:
                deleteMooyo(i, j, val)  # K개보다 많아지면 삭제
                flag = True

    if not flag:  # 더이상 삭제할 것이 없는 지 확인
        break

    Down()  # 내려오기

for i in Map:
    print(''.join(i))
