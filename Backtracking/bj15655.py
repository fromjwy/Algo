N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
lst.insert(0,0)
visited = [0]*(N+1)
result = []

#조합
def DFS(L, S):
    if L == M:
        print(' '.join(result))
        return

    for i in range(S, N+1):
        if visited[i]:
            continue

        result.append(str(lst[i]))
        visited[i] = 1
        DFS(L+1, i+1)
        result.pop()
        visited[i] = 0


DFS(0, 1)