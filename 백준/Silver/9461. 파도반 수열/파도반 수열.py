t = int(input())
dp = [0] * 101
dp[0] = 0
dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2

for _ in range(t):
    n = int(input())
    for i in range(5, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])
