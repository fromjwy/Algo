tc = int(input())

for _ in range(tc):
    # lStack Cursor rStack 구조로 문자를 하나씩 좌우이동
    lStack = []
    rStack = []  # insert(0) 연산 사용하지 않기 위해 Heap 대신 Stack 사용

    string = input()

    for s in string:
        if s == '<':
            if lStack:
                rStack.append(lStack.pop())
        elif s == '>':
            if rStack:
                lStack.append(rStack.pop())
        elif s == '-':
            if lStack:
                lStack.pop()
        else:
            lStack.append(s)

    lStack.extend(reversed(rStack))  # 마지막에 rStack 뒤집기
    print(''.join(lStack))
