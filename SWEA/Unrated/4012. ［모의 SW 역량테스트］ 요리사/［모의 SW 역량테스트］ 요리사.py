def dfs(n, alst, blst):
    global ans
    if n == N: #n은 N개까지
        if len(alst) == M: #배열의 길이가 M이되면 종료
            asum = bsum = 0 # 합들은 일단 0으로 해놓음
            for i in range(M):
                for j in range(M):
                    asum += source[alst[i]][alst[j]]
                    bsum += source[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))
        return
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst,blst+[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N//2 # 배열의 길이
    source = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000* N * N # 답의 최댓값
    dfs(0,[],[])
    print(f'#{tc} {ans}')