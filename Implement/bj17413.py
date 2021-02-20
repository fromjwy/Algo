S, tmp = input(), ''

ck = False #'<'가 True이면 아직 안 닫힌 상태
ans = ''

for i in S:
    if i == '<':
        ck = True
        ans += tmp[::-1]+'<'
        tmp = ''
    elif i == '>':
        ck = False
        ans += '>'
    elif i == ' ':
        if ck:
            ans += ' '
        else:
            ans += tmp[::-1]+' '
            tmp = ''
    else:
        if ck:
            ans += i
        else:
            tmp += i

print(ans)
