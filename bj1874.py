
n = int(input())
stack = []
result = []

cnt = 1

# 입력 개수만큼 반복
for _ in range(n):
    num = int(input())
    # 현재 입력값까지 cnt를 stack에 삽입
    while num >= cnt:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    # 현재 입력값과 stack top이 같으면 삭제, 다르면 예외처리
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

# stack 수열 가능한 경우 출력
for i in range(len(result)):
    print(result[i])
