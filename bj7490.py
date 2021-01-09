import copy

def addOp(op, n):
    if len(op) == n:
        op_list.append(copy.deepcopy(op))
        return

    op.append(' ')
    addOp(op, n)
    op.pop()

    op.append('+')
    addOp(op, n)
    op.pop()

    op.append('-')
    addOp(op, n)
    op.pop()


tc = int(input())

for _ in range(tc):
    n = int(input())
    num_list = [i for i in range(1, n+1)]
    op_list = []

    addOp([], n-1)
    # print(op_list)

    for op in op_list:
        tmp = ""
        for i in range(n-1):
            tmp += str(num_list[i]) + op[i]
        tmp += str(num_list[-1])

        if eval(tmp.replace(" ", '')) == 0:
            print(tmp)

    print()
