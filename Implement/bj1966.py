
tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    # 각 중요도가 몇번째 원소인지 표시하기 위한 index 할당
    q = [(i, idx) for idx, i in enumerate(q)]

    cnt = 0
    while True:
        # Queue에 첫번째 원소가 리스트에서 가장 큰 원소이면
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            cnt += 1
            # 첫번째 원소의 index가 타겟 index라면
            if q[0][1] == m:
                print(cnt)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))
