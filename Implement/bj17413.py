S, tmp = input(), ''

ck = False
ans = ''

for i in S:
    if i == ' ':
        if ck:
            ans += ' '
        else:
            ans += tmp[::-1]+' '
            tmp = ''
    elif i == '<':
        ck = True
        ans += tmp[::-1]+'<'
        tmp = ''
    elif i == '>':
        ck = False
        ans += '>'
    else:
        if ck:
            ans += i
        else:
            tmp += i

print(ans)
