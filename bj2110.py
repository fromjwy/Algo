N, C = map(int, input().split())
home = []

for _ in range(N):
    home.append(int(input()))

home.sort()

min_gap, max_gap = 1, home[-1]-home[0]
result = 0

while min_gap <= max_gap:
    mid = (min_gap+max_gap)//2

    # 설치 가능한 공유기 수 구하기
    cnt = 1
    idx = 0
    for i in range(1, N):
        if home[i] - home[idx] >= mid:
            cnt += 1
            idx = i

    # 공유기 수가 조건과 같으면 결과와 min_gap 업데이트
    if cnt >= C:
        min_gap = mid+1
        result = mid
    else:
        max_gap = mid-1

print(result)
