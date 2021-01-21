import heapq

N = int(input())
D_R = []

for i in range(N):
    D, R = map(int, input().split())
    D_R.append([i+1, D, R])

# 데드라인을 기준으로 정렬
D_R.sort(key=lambda x: (x[1]))

result = []

for p in D_R:
    heapq.heappush(result, p[2])
    # 풀려고 하는 문제 수가 현재 데드라인보다 크면 가장 적은 라면 문제 제거
    if len(result) > p[1]:
        heapq.heappop(result)

print(sum(result))
