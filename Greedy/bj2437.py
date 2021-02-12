N = int(input())
lst = sorted(list(map(int, input().split())))

result = 0
for x in lst:
    if x <= result+1:
        result += x
    else:
        break


print(result+1)
 