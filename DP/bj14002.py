N = int(input())
num = list(map(int, input().split()))

DP = [1]*N # 자기 자신이 최대 증가부분 수열일 수 있기 때문에
path = [i for i in range(N)]

idx = 0
for i in range(1, N):
    for j in range(0, i):
        if num[i] > num[j]:
            DP[i] = max(DP[i], DP[j]+1)
            path[i] = j

print(max(DP))


res = []
maxVal = max(DP)
for i in range(N-1, -1, -1):
    if DP[i] == maxVal:
        res.append(num[i])
        maxVal -= 1
res.reverse()
print(*res)