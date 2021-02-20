def find(v):
    if v == parents[v]:
        return v
    else:
        new_parent = find(parents[v])
        parents[v] = new_parent
        return parents[v]


def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[py] = px
        network[px] += network[py]


tc = int(input())

for _ in range(tc):
    F = int(input())

    parents = dict()  # me:parent
    network = dict()

    for _ in range(F):
        x, y = input().split()

        # 처음 등장하는 친구인 경우 부모를 자기 자신으로 초기화
        if x not in parents:
            parents[x] = x
            network[x] = 1
        if y not in parents:
            parents[y] = y
            network[y] = 1

        # 합집합 만들기
        union(x, y)

        print(network[find(x)])
