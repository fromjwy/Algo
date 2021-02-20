T = int(input())

for _ in range(T):
    N, C = int(input()), list(map(int, input().split()))
    cnt = 0

    while True:
        # 만약 이 결과 홀수개의 사탕을 가지게 된 아이가 있을 경우 선생님이 한 개를 보충해 짝수로 만들어 주기로 했다.
        # 홀수가 있으면 +1
        for i in range(N):
            if C[i] % 2 == 1:
                C[i] += 1

        # 이 과정을 몇 번 거치자 자연스럽게 모든 아이들이 같은 수의 사탕을 가지게 되어 소란은 종료되었다.
        # 현재 모두 같으면 break
        if len(set(C)) == 1:
            break

        # 모든 아이들은 동시에 자기가 가지고 있는 사탕의 절반을 오른쪽 아이에게 준다.
        # 반으로 나눠서 오른쪽에 전달, cnt++
        ban = [0 for _ in range(N)]
        for i in range(N):
            C[i] //= 2
            ban[(i+1) % N] = C[i]

        for i in range(N):
            C[i] += ban[i]

        cnt += 1

    print(cnt)
