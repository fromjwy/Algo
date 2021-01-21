import sys

N, K = int(input()), int(input())
censor = list(map(int, input().split()))

# 센서보다 최대 집중국 수가 더 크거나 같으면
if N <= K:
    print(0)
    sys.exit(0)

censor.sort()

dist = []
for i in range(1, N):
    dist.append(censor[i]-censor[i-1])

# 거리가 가장 긴것부터 K-1번 센서 그룹 나누기
dist.sort(reverse=True)
for i in range(K-1):
    dist[i] = 0

print(sum(dist))
