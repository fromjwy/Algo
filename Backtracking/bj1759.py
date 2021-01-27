from itertools import combinations
import copy

L, C = map(int, input().split())

alpha = list(input().split())
alpha.sort()

vowels = ['a', 'e', 'i', 'o', 'u']

'''
#암호 길이가 L인 모든 조합 중에서
for pw in combinations(alpha, L):
    cnt = 0
    for i in pw:
        if i in vowels:
            cnt += 1
    #모음의 개수가 최소 1개, 자음의 개수 최소 2개인 경우만 출력
    if cnt >= 1 and cnt <= L-2:
        print(''.join(pw))
'''
result = []
string = []
visited = [False for _ in range(C)]


def DFS(idx):
    if len(string) == L:
        result.append(copy.deepcopy(string))
    else:
        for i in range(idx, C):
            if not visited[i]:
                visited[i] = True
                string.append(alpha[i])
                DFS(i+1)
                visited[i] = False
                string.pop()


DFS(0)
# 암호 길이가 L인 모든 조합 중에서
for pw in result:
    cnt = 0
    for i in pw:
        if i in vowels:
            cnt += 1
    # 모음의 개수가 최소 1개, 자음의 개수 최소 2개인 경우만 출력
    if cnt >= 1 and cnt <= L-2:
        print(''.join(pw))
