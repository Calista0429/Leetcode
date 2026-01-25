def zeroonepack2D(weights, values, capacity):
    n = len(weights)
    #2D DP array
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j < weights[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                # Not taking the item: dp[i - 1][j]
                # Taking the item: dp[i - 1][j - weights[i - 1]] + values[i - 1]
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]



weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 4
print(zeroonepack2D(weights, values, capacity))  # Output: 50