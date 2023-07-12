N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
cnt = [[0] * 101 for _ in range(101)]

black_area = 0
double_area = 0


for i in range(N):
    x1 = square[i][0]
    y1 = square[i][1]
    x2 = square[i][0] + 10
    y2 = square[i][1] + 10

    for k in range(x1, x2):
        for j in range(y1, y2):
            if cnt[k][j] == 0:
                cnt[k][j] = 1
                black_area += 1
            else:
                cnt[k][j] = 2
                double_area += 1

print(black_area)
