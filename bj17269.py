N, M = map(int, input().split())
A, B = input().split()

alpha = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3,
         'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}


# 알파벳 번걸아 적고 숫자로 변환
alphaToNum = ''
min_len = min(N, M)
for i in range(min_len):
    alphaToNum += A[i] + B[i]

alphaToNum += A[min_len:] + B[min_len:]

result = []
for i in range(len(alphaToNum)):
    result.append(alpha[alphaToNum[i]])


# 숫자가 2개 남을 때까지 2개씩 더하기
while True:
    if len(result) == 2:
        break

    tmpList = result
    result = []
    for i in range(1, len(tmpList)):
        tmp = tmpList[i-1]+tmpList[i]
        # 더한 숫자가 10보다 크면 나머지 값으로 변경
        if tmp >= 10:
            tmp %= 10

        result.append(tmp)

print(str(int(str(result[0])+str(result[1])))+'%')
