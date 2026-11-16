def uniquePaths(m: int, n: int) -> int:
    dp = [([0] * n) for _ in range(m)]
    dp[0][0] = 1
    print(dp)
uniquePaths(m=3, n=7)