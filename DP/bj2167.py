N, M = map(int, input().split())
num = [[0] + list(map(int, input().split())) for _ in range(N)]
num.insert(0, [0]*(M+1))
DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + num[i][j]
        # DP[i-1][j-1] -> 두번 더해진 교집합을 뺀다

K = int(input())
for i in range(K):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])
    # DP[i-1][j-1] -> 두번 빼진 교집합을 더한다
