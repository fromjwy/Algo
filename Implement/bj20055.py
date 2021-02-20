import sys
from collections import deque
n, k = map(int, input().split())
A = deque(list(map(int, input().split())))

ans = 0

robot = deque(list([0]*(n*2)))

# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
while True:
    ans += 1

    # 1단계 벨트가 한 칸 회전한다.
    A.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0  # 마지막 로봇이 벨트에서 내려감.

    # 2단계 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1, -1):

        if robot[i] == 1 and robot[i+1] == 0 and A[i+1] > 0:
            robot[i] = 0 
            robot[i+1] = 1
            A[i+1] -= 1

    robot[n-1] = 0 #마지막 로봇이 벨트에서 내려감.

    # 3단계 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and A[0] > 0:
        robot[0] = 1
        A[0] -= 1

    # 4단계
    if A.count(0) >= k:
        break

print(ans)
