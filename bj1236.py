N, M = map(int, input().split())

castle = [list(map(str, input())) for _ in range(N)]
# print(castle)

row_cnt, col_cnt = 0, 0

# 행 체크
for row in castle:
    if 'X' not in row:
        row_cnt += 1

# 열 체크
for i in range(M):
    check = False
    for j in range(N):
        if castle[j][i] == 'X':
            check = True
            break

    if check == False:
        col_cnt += 1

print(max(row_cnt, col_cnt))
