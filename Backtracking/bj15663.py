N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
lst.insert(0,0)
visited = [0]*(N+1)
result = []
tmp = ''

#순열
def DFS(L):
    global tmp
    if L == M:
        print(' '.join(result))
        return

    for i in range(1, N+1):
        if visited[i] or tmp == str(lst[i]):
            continue
        
        tmp = ''
        result.append(str(lst[i]))
        visited[i] = 1
        DFS(L+1)
        tmp = result.pop()
        visited[i] = 0


DFS(0)
