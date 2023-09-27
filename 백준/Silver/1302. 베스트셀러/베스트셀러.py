N = int(input())
book_dict = {}

for i in range(N):
    book = input()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1
max_v = max(book_dict.values())

best = []
for k,v in book_dict.items():
    if v == max_v:
        best.append(k)
best = sorted(best)
print(best[0])