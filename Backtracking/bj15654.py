N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
result = []
visited = [0]*(N+1)

# 순열
def DFS(L):
    if L == M:
        print(' '.join(result))
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        result.append(str(lst[i-1]))
        visited[i] = 1
        DFS(L+1)
        result.pop()
        visited[i] = 0


DFS(0)
