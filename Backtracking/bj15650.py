N, M = map(int, input().split())
lst = []

#조합
def DFS(L, S):
    if L == M:
        print(' '.join(lst))
        return

    for i in range(S, N+1):

        lst.append(str(i))
        DFS(L+1, i+1)
        lst.pop()


DFS(0, 1)
