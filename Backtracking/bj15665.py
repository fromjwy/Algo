N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
lst.insert(0, 0)
result = []
tmp = ''


# 중복순열
def DFS(L):
    global tmp
    if L == M:
        print(' '.join(result))
        return

    for i in range(1, N+1):
        if tmp == str(lst[i]):
            continue

        tmp = ''
        result.append(str(lst[i]))
        DFS(L+1)
        tmp = result.pop()


DFS(0)
