N = int(input())

books = {}

for _ in range(N):
    book = input()
    books[book] = books.get(book, 0)+1

target = max(books.values())

# 팔린 개수가 같은 것들 중 사전순 먼저 오는 것
cand = []
for book, cnt in books.items():
    if cnt == target:
        cand.append(book)

print(sorted(cand)[0])
