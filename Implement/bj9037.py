T = int(input())

for _ in range(T):
    N, C = int(input()), list(map(int, input().split()))
    cnt = 0

    while True:
        # 홀수가 있으면 +1
        for i in range(N):
            if C[i] % 2 == 1:
                C[i] += 1

        # 현재 모두 같으면 break
        if len(set(C)) == 1:
            break

        # 반으로 나눠서 오른쪽에 전달, cnt++
        ban = [0 for _ in range(N)]
        for i in range(N):
            C[i] //= 2
            ban[(i+1) % N] = C[i]

        for i in range(N):
            C[i] += ban[i]

        cnt += 1

    print(cnt)
