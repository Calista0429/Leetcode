from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(len(coins) - 1, -1, -1):
        for j in range(coins[i], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1 )
    return dp[-1]
coins = [1,2,5]
amount = 11
coinChange(coins, amount)