N = int(input())
num = list(map(int, input().split()))

table = [1]*N

for i in range(1, N):
    for j in range(0, i):
        if num[i] > num[j]:
            table[i] = max(table[i], table[j]+1)

print(max(table))