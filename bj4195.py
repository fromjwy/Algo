def find(x):
    if x == parents[x]:
        return x
    else:
        parent = find(parents[x])
        parents[x] = parent
        return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[py] = px
        network[px] += network[py]


tc = int(input())

for _ in range(tc):
    F = int(input())

    parents = dict()
    network = dict()

    for _ in range(F):
        x, y = input().split()

        # 처음엔 자기 자신을 부모로 초기화
        if x not in parents:
            parents[x] = x
            network[x] = 1
        if y not in parents:
            parents[y] = y
            network[y] = 1

        # 합집합 만들기
        union(x, y)

        print(network[find(x)])
