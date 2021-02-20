import heapq

N = int(input())
heap = []
result = []
heapq.heapify(heap)

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            # 배열에서 가장 작은 값을 제거한다.
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        # 배열에 자연수 x를 넣는다.
        heapq.heappush(heap, x)


for x in result:
    print(x)
