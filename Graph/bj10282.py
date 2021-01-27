import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        sum_dist, now = heapq.heappop(heap)
        if dist[now] < sum_dist:
            continue

        for v in adj[now]:
            cost = sum_dist+v[1]
            if dist[v[0]] > cost:
                dist[v[0]] = cost
                heapq.heappush(heap, (cost, v[0]))


tc = int(input())

for _ in range(tc):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    dist = [1e9]*(n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))

    dijkstra(c)

    cnt=0
    max_dist = 0
    for d in dist:
        if d != 1e9:
            cnt+=1
            if d > max_dist:
                max_dist = d

    print(cnt, max_dist)