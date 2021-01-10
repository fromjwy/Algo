from collections import deque

tc = int(input())

for _ in range(tc):
    # left Cursor right 구조로 문자를 하나씩 좌우이동

    left = deque()
    right = deque()

    string = input()

    for s in string:
        if s == '<':
            if left:
                right.appendleft(left.pop())
        elif s == '>':
            if right:
                left.append(right.popleft())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)

    left.extend(right)
    print(''.join(left))
