N = int(input())
tri = [[0]+list(map(int, input().split()))+[0] for _ in range(N)]
tri.insert(0, [0,0])
DP = [[0]*len(tri[i]) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1,len(tri[i])-1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + tri[i][j]

print(max(DP[-1]))