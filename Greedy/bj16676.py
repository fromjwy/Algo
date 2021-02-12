N = input()
S = '1'*len(N)

if len(N) == 1:  # 예외 : 값이 0일 때
    print(1)
elif int(N) < int(S):
    print(len(N)-1)
else:
    print(len(N))
