from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

result = 0

#같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
def slide(lst, N):
    TmpList = [i for i in lst if i]  # 0이 아닌 숫자들만
    for i in range(1, len(TmpList)):
        if TmpList[i-1] == TmpList[i]:
            TmpList[i-1] *= 2
            TmpList[i] = 0

    NewList = [i for i in TmpList if i]  # 0이 아닌 숫자들만
    return NewList + [0]*(N-len(NewList))


def rotate90(N, OldBoard):
    NewBoard = deepcopy(OldBoard)
    for i in range(N):
        for j in range(N):
            NewBoard[j][N-i-1] = OldBoard[i][j]

    return NewBoard

#한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
def move(N, board, cnt):
    result = max([max(i) for i in board])
    if cnt == 0:
        return result

    # 상하좌우 방향 각각 같은 블록이 있으면 합쳐서 왼쪽으로 밀기
    for _ in range(4):
        # 보드가 0, 90, 180, 270 회전한 상태에서 왼쪽으로 밀어서 만든 임시
        TmpBoard = [slide(X, N) for X in board]
        # 가장 큰 블록 갱신
        result = max(result, move(N, TmpBoard, cnt-1))
        # 보드 회전
        board = rotate90(N, board)

    return result


# 5번 이동 후 결과
print(move(N, Board, 5))
