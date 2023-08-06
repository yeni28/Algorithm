N = int(input())

# 가장 큰 수인 5로 먼저 담는 것이 가장 작은 봉투 개수를 만들 수 있는 비결
if N % 5 == 0:
    ans = N // 5
    print(ans)
else:
    sugar = 0
    # N을 나눌 수 있을 때 까지
    while N > 0:
        # 3키로 봉지를 빼면서
        N -= 3
        # 봉지 개수 하나 씩 늘이기
        sugar += 1
        # 5키로도 할 수 있다면?
        if N % 5 == 0:
            sugar += N // 5
            print(sugar)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(sugar)
            break

