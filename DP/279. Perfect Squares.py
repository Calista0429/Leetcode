def numSquares(n: int) -> int:
    dp = [float('inf') for _ in range(n + 1)]
    dp[0], dp[1] = 0, 1

    # for num in range(n // 2):
    #     for i in range(2, n+1):
    #         if i >= (num ** 2):
    #             dp[i] = min(dp[i], dp[i - (num ** 2)] + 1)
    

    for i in range(1, n + 1):
        for j in range(n//2):
            if i >= j ** 2:
                dp[i] = min(dp[i], dp[i - (j**2)] + 1)
    return dp[n]
n = 2
numSquares(n=n)


    