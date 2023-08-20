T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    if R <= W:
        price = (W-R) * S + Q
    else:
        price = Q
    a_price = W * P
    ans = min(price, a_price)
    print(f'#{tc} {ans}')