str1 = input()
str2 = input()
n1, n2 = len(str1), len(str2)

table = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        # 현재 문자가 서로 같으면 왼쪽 대각선 위+1, 다르면 위쪽 또는 왼쪽 중 더 큰값
        if str1[i-1] == str2[j-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])


print(table[n1][n2])
