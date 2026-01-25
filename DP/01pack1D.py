def zeroone1D(weights, values, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 4
print(zeroone1D(weights, values, capacity))  # Output: 50