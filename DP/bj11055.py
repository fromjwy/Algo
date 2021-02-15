import copy

N = int(input())
num = list(map(int, input().split()))
DP = copy.deepcopy(num)  # 자기 자신이 최대 증가부분 수열일 수 있기 때문에

for i in range(1, N):
    for j in range(0, i):
        if num[i] > num[j]:
            DP[i] = max(DP[i], DP[j] + num[i])


print(max(DP))
