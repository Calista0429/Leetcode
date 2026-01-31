from typing import List
def change(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    # 组合数
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] += dp[i - coin]
    
    # 排列数
    # for coin in coins:
    #     for i in range(coin, amount + 1):
    #         dp[i] += dp[i - coin]
    return dp[amount] if dp[amount] > 0 else 0
change(amount = 5, coins = [1,2,5])
