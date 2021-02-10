N, M = map(int, input().split())
lst = []
visited = [0]*(N+1)

#순열
def DFS(L):
    if L == M:
        print(' '.join(lst))
        return

    for i in range(1,N+1):
        if visited[i]:
            continue

        lst.append(str(i))
        visited[i] = 1
        DFS(L+1)
        lst.pop()
        visited[i] = 0


DFS(0)

