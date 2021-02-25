N, M = map(int, input().split())
lst = []

# 중복순열

def DFS(L):
    if L == M:
        print(' '.join(lst))
        return

    for i in range(1, N+1):

        lst.append(str(i))
        DFS(L+1)
        lst.pop()


DFS(0)
