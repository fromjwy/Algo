import heapq
import copy

K, N = map(int, input().split())
lst = list(map(int, input().split()))

heap = copy.deepcopy(lst)
ck = set()

heapq.heapify(heap)
ith = 0
min_ = 0

while ith < N:
    min_ = heapq.heappop(heap)
    if min_ in ck:
        continue
    ith+=1
    ck.add(min_)

    for x in lst:
        if min_*x < 2**32:
            heapq.heappush(heap, min_*x)

print(min_)