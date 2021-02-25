N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
lst.insert(0, 0)
result = []

# 조합
def DFS(L, S):
    if L == M:
        print(' '.join(result))
        return

    for i in range(S, N+1):
        result.append(str(lst[i]))
        DFS(L+1, i+1)
        result.pop()


DFS(0, 1)
