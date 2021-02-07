from collections import deque
#import sys
# sys.setrecursionlimit(10000)

N, K = map(int, input().split())
Map = [list(input()) for _ in range(N)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


def countMooyo(x, y):
    cnt = 1
    q1 = deque([(x, y)])
    ck[x][y] = True

    while q1:
        x, y = q1.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= 10:
                continue

            if ck[nx][ny] or Map[x][y] != Map[nx][ny]:
                continue

            q1.append((nx, ny))
            ck[nx][ny] = True

            cnt += 1
    return cnt


def deleteMooyo(x, y, val):

    q2 = deque([(x, y)])
    ck2[x][y] = True

    while q2:
        x, y = q2.popleft()
        Map[x][y] = '0'

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= 10:
                continue

            if ck2[nx][ny] or Map[nx][ny] != val:
                continue

            q2.append((nx, ny))
            ck2[nx][ny] = True


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

            mooyo = countMooyo(i, j)  # 그룹의 갯수 세기

            if mooyo >= K:
                deleteMooyo(i, j, Map[i][j])  # K개보다 많아지면 삭제
                flag = True

    if not flag:  # 더이상 삭제할 것이 없는 지 확인
        break

    Down()  # 내려오기

for i in Map:
    print(''.join(i))
