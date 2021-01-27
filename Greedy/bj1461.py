import heapq

N, M = map(int, input().split())
minus = []
plus = []
numbers = list(map(int, input().split())) 
largest = max(max(numbers), -min(numbers))


#Max heap 구성
for num in numbers:
    if num > 0:
        heapq.heappush(plus, -num)
    else:
        heapq.heappush(minus, num)

result = 0

while minus:
    result+=heapq.heappop(minus)
    for _ in range(M-1):
        if minus:
            heapq.heappop(minus)

while plus:
    result+=heapq.heappop(plus)
    for _ in range(M-1):
        if plus:
            heapq.heappop(plus)

print(-result*2-largest)


