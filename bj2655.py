N = int(input())
dols = [[i+1] + list(map(int, input().split())) for i in range(N)]
dols.sort(key=lambda x: x[3])  # 무게를 기준으로 정렬
dols.insert(0, [0, 0, 0, 0])

table = [0]*(N+1)

for i in range(1, N+1):
    for j in range(0, i):
        # 넓이를 기준으로 현재 벽돌이 지난 벽돌 밑에 놓일 수 있는지 확인
        if dols[i][1] > dols[j][1]:
            table[i] = max(table[i], table[j]+dols[i][2])

max_value = max(table)
index = N
result = []

# 역산해서 쌓았던 벽돌 번호 탐색
while index != 0:
    if max_value == table[index]:
        result.append(dols[index][0])
        max_value -= dols[index][2]

    index -= 1

print(len(result))
[print(i) for i in result[-1::-1]]
