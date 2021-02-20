from collections import deque

tc = int(input())

for _ in range(tc):
    # left Cursor right 구조로 문자를 하나씩 좌우이동

    left = deque()
    right = deque()

    string = input()

    for s in string:
        # 화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다.
        if s == '<':
            if left:
                right.appendleft(left.pop())
        elif s == '>':
            if right:
                left.append(right.popleft())
        # 강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다.
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)

    left.extend(right)
    print(''.join(left))
