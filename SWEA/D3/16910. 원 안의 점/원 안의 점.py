T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    # -N에서 N까지 (지름)
    for i in range(-N, N+1):
        for j in range(-N, N+1):
         	# 만약 x*x + y*y <= N*N이라면, 
            if i*i + j*j <= N * N:
                # 거기서 격자점 개수를 센다!
                cnt += 1
    print(f'#{tc} {cnt}')                