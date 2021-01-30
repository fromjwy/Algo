N = int(input())
result = []

for _ in range(N):
    tmp = sorted(list(map(int, input().split())))

    # 다 같은 경우
    if len(set(tmp)) == 1:
        result.append(50000+tmp[0]*5000)
    if len(set(tmp)) == 2:
        # 세개만 같은 경우
        if tmp[1] == tmp[2]:
            result.append(10000+tmp[1]*1000)
        # 두개씩 두쌍인 경우
        else:
            result.append(2000+tmp[0]*500+tmp[2]*500)
    # 두개만 같은 경우
    if len(set(tmp)) == 3:
        for i in range(3):
            if tmp[i] == tmp[i+1]:
                result.append(1000 + tmp[i]*100)
    # 모두 다른 경우
    if len(tmp) == len(set(tmp)):
        result.append(max(tmp)*100)


print(max(result))
