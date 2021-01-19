def promising(x):
    for i in range(x):
        # 위쪽 체크
        if row[x] == row[i]:
            return False
        # 대각선 체크
        if abs(row[x] - row[i]) == x - i:
            return False
    return True


def DFS(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            # Queen을 놓을 수 있으면
            if promising(x):
                DFS(x+1)


N = int(input())
row = [0] * N
result = 0
DFS(0)
print(result)
