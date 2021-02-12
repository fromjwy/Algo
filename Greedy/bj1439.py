S = input()
result = 0

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        result+=1

print((result+1)//2)