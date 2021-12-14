d = dict()

n = int(input())
for _ in range(n):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

max_cnt = max(d.values())
max_book = []
for k, v in d.items():
    if v == max_cnt:
        max_book.append(k)

print(sorted(max_book)[0])
