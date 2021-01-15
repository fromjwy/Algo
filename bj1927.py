import heapq

N = int(input())
heap = []
result = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, num)


for num in result:
    print(num)