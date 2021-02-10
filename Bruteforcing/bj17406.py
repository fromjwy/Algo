from copy import deepcopy

N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Q = [list(map(int, input().split())) for _ in range(K)]

result = 987654321

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def getValue(arr):
    return min([sum(x) for x in arr])


def rotate(arr, q):
    r, c, s = q
    r, c = r-1, c-1

    newArr = deepcopy(arr)

    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):  # 상하좌우
            for _ in range(i*2):  # 중심점에서 멀어진 거리에 2배만큼 이동
                rrr, ccc = rr + dx[w], cc + dy[w]
                newArr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc

    return newArr


def DFS(arr, q):
    global result
    if sum(q) == K:
        result = min(result, getValue(arr))  # 배열 값 구하기, 행마다 합 구해서 최소값 갱신
        return

    for i in range(K):
        if q[i]:
            continue

        newArr = rotate(arr, Q[i])  # 회전
        q[i] = 1
        DFS(newArr, q)
        q[i] = 0


DFS(Map, [0 for i in range(K)])
print(result)
