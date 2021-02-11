N, M = map(int, input().split())
lst = []
visited = [0]*(N+1)

# 중복조합
def DFS(L, S):
    if L == M:

        print(' '.join(lst))
        return

    for i in range(S, N+1):
        if visited[i]:
            continue

        lst.append(str(i))
        DFS(L+1, i)
        lst.pop()


DFS(0, 1)
