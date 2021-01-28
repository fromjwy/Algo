import heapq
N = int(input())

cards = []
for _ in range(N):
    card = int(input())
    heapq.heappush(cards, card)

result = 0
while len(cards)>1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    tmp = A+B
    result +=tmp
    heapq.heappush(cards, tmp)

print(result)