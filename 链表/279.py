import math
def numSquares(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(math.isqrt(i)):
            if i >= j * j:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[n]
numSquares(12)