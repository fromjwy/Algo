from copy import deepcopy
import sys
sys.setrecursionlimit(1000)

N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Q = [list(map(int, input().split())) for _ in range(K)]

result = 987654321

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 남, 서, 북, 동


def getValue(arr):
    return min([sum(x) for x in arr])


def rotate(arr, q):
    r, c, s = q
    r, c = r-1, c-1

    newArr = deepcopy(arr)

    for i in range(1, s+1):  # 상방향 오른쪽 대각선 거리(상하좌우 회전 횟수)
        rr, cc = r-i, c+i  # 상방향 오른쪽 대각선 한칸 이동
        for w in range(4):  # 상하좌우
            for _ in range(i*2):  # 중심점에서 멀어진 거리에 2배만큼 한칸씩 이동
                rrr, ccc = rr + dx[w], cc + dy[w]
                newArr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc  # 기준점 한칸씩 이동

    return newArr


def DFS(arr, ck):
    global result
    if sum(ck) == K:
        result = min(result, getValue(arr))  # 배열 값 구하기, 행마다 합 구해서 최소값 갱신
        return

    for i in range(K):
        if ck[i]:
            continue

        newArr = rotate(arr, Q[i])  # 회전
        ck[i] = 1
        DFS(newArr, ck)
        ck[i] = 0


DFS(Map, [0 for i in range(K)])
print(result)
