def integerBreak(n: int) -> int:
    #DP的含义：数字为i拆分后的最大乘积
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1], dp[2] = 0, 0, 1
    for i in range(n + 1):
        for j in range(i):
            ## 递推公式：当拆分成两个时候j * (i-j), 当拆分成三个或者三个以上时j * dp[i-j]
            dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
    return dp[-1]
    