N, S, M = map(int, input().split())
V = list(map(int, input().split()))

table = [[False]*(M+1) for _ in range(N+1)]
table[0][S] = True

for i in range(1, N+1):
    for j in range(M+1):
        # 이전 위치했던 볼륨에서만 재조정 가능
        if table[i-1][j] == False:
            continue
        minus = j - V[i-1]
        plus = j + V[i-1]
        if minus >= 0:
            table[i][minus] = True
        if plus <= M:
            table[i][plus] = True


result = -1
for i in range(M, -1, -1):
    if table[N][i] == True:
        result = i
        break

print(result)
