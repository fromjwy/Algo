N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
lst.insert(0, 0)
result = []
tmp = ''


# 중복조합
def DFS(L, S):
    global tmp
    if L == M:
        print(' '.join(result))
        return

    for i in range(S, N+1):
        if tmp == str(lst[i]):
            continue

        tmp = ''
        result.append(str(lst[i]))
        DFS(L+1, i)
        tmp = result.pop()


DFS(0, 1)
