import sys

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

if max(crane) < max(box):
    print(-1)
    sys.exit()

crane.sort(reverse=True)
box.sort(reverse=True)

result = 0
# 박스를 다 옮길 때까지 반복
while box:
    result += 1
    # 각 크레인에 대해서
    for i in range(N):
        if not box:
            break
        # 남은 박스에 대해서 현재 크레인에 옮길 수 있으면 제거
        for j in range(len(box)):
            if box[j] <= crane[i]:
                box.pop(j)
                break


print(result)
