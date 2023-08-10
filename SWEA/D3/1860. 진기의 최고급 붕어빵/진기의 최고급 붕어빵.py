T = int(input())

for t in range(1, T+1):
    n,m,k = map(int, input().split())
    customer = list(map(int,input().split()))
    #빨리 오는 순으로 정렬
    customer.sort()
    #제일 늦게 오는 사람
    last = int(customer[-1]) + 1
    # 붕어빵
    fish_bread = 0
    check = 0
    
    for i in range(0, last):
        # 빵굽자구
        if i != 0 and i % m == 0:
            fish_bread += k
       	#손님이 온 시간대인지 확인
        if i in customer:
                fish_bread -= 1
        if fish_bread < 0:
                check += 1
    if check:
        ans = 'Impossible'
    else:
        ans = 'Possible'
        
    print(f'#{t} {ans} ')
            