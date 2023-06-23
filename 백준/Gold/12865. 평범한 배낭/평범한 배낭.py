N, K = map(int, input().split())
stuff = [[0,0]] #[[6, 13], [4, 8], [3, 6], [5, 12]]
dp = [[0] *(K+1) for i in range(N+1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))


for i in range(1,N+1):
    for j in range(1, K+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j] )

print(dp[N][K])