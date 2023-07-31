T = int(input())
for _ in range(T):
    i = int(input())
    cnt = [0] * 1000
    scores = list(map(int, input().split()))
    for score in scores:
        cnt[score] += 1
    max_num = max(cnt)
    max_index = 0
    for index, count in enumerate(cnt):
        if count == max_num:
            max_index = index
    print(f'#{i} {max_index}')
        