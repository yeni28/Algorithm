n = int(input())
tr = []
for _ in range(n):
    a = list(map(int, input().split()))
    tr.append(a)

for i in range(n):
    for j in range(i+1):
        if i == 0:
            tr[i][j] = tr[i][j]
            continue
        if j == 0:
            up = tr[i-1][0]
            tr[i][j] += tr[i-1][0]
            continue
        if j == i :
            left = tr[i-1][j-1]
            tr[i][j] += tr[i-1][j-1]
            continue

        else:
            up_left = tr[i-1][j-1]
            up_right = tr[i-1][j]
            tr[i][j] += max(up_left, up_right)

result = 0
for j in range(n):
    result = max(result, tr[n-1][j])
print(result)