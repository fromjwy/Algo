N = int(input())

Tile = [0] * 1000001  # N의 최대 범위까지 미리 초기화

Tile[1] = 1
Tile[2] = 2

for i in range(3, N+1):
    Tile[i] = (Tile[i-2] + Tile[i-1]) % 15746

print(Tile[N])
