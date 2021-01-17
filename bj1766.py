import heapq

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
prob = []
result = []

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B]+=1 #진입차수

#heap에 진입차수가 0인 정점을 push
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(prob, i)

#heap에서 pop, 제거한 정점의 adj들 indegree 제거
while prob:
    a = heapq.heappop(prob)
    result.append(a)
    for b in adj[a]:
        indegree[b]-=1
        if indegree[b] == 0:
            heapq.heappush(prob, b)


for a in result:
    print(a, end=' ')


