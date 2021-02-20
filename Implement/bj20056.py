from collections import deque

N, M, K = map(int, input().split())
# (r,c) i번 파이어볼의 위치, m 질량, s 속력, d 방향
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
Map = [[[] for _ in range(N)] for _ in range(N)]
tmp = []

# 초기상태
# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    Map[r-1][c-1].append([r, c, m, s, d])

for _ in range(K):
    tmp = []  # 이번에 이동시킬 파이어볼 정보 저장
    for i in range(N):
        for j in range(N):
            if Map[i][j] != []:
                tmp += Map[i][j]

    # 1 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    # 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
    for q in range(len(tmp)):
        r, c, m, s, d = tmp[q]
        nx, ny = (r+(dx[d]*s)) % N, (c+(dy[d]*s)) % N #범위를 넘어가면 모듈러 연산
        Map[nx-1][ny-1].append([nx, ny, m, s, d])
        Map[r-1][c-1].remove([r, c, m, s, d])

    # 2 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    # 파이어볼은 4개의 파이어볼로 나누어진다.
    # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
    # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
    # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
    # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    # 질량이 0인 파이어볼은 소멸되어 없어진다.

    for i in range(N):
        for j in range(N):
            if len(Map[i][j]) >= 2: #같은 위치에 파이어볼 2개 이상이면
                nm, ns, nd = 0, 0, []
                for k in range(len(Map[i][j])):
                    nm += Map[i][j][k][2]
                    ns += Map[i][j][k][3]
                    nd.append(Map[i][j][k][4] % 2)

                nm //= 5
                ns //= len(Map[i][j])

                if nm != 0:
                    Map[i][j] = [] #원래 있던 파이어볼 정보 제거
                    if len(set(nd)) == 1:
                        t = 0
                    else:
                        t = 1
                    for e in range(4): #4개로 쪼개진 파이어볼 정보 추가
                        Map[i][j].append([i+1, j+1, nm, ns, t+2*e])
                else:
                    Map[i][j] = [] #질량이 0인 파이어볼 소멸


# 3 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(len(Map[i][j])):
            ans += Map[i][j][k][2]

print(ans)
