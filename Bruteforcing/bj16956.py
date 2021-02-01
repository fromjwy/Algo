from collections import deque
import sys
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
ck = False

for i in range(R):
    for j in range(C):
        if Map[i][j] == 'W':
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if nx < 0 or nx == R or ny < 0 or ny == C:
                    continue

                if Map[nx][ny] == 'S':
                    ck = True

        elif Map[i][j] == '.':
            Map[i][j] = 'D'

if ck:
    print(0)
else:
    print(1)
    for a in Map:
        print(''.join(a))