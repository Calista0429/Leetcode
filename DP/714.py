from typing import List
def maxProfit(prices: List[int], fee: int) -> int:
    dp = [[0 for i in range(2)] for j in range(len(prices))]
    #持有
    dp[0][0] = -prices[0]
    #不持有
    dp[0][1] = 0
    for i in range(1, len(prices)):
        #持有：一直持有；当天持有
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        #不持有：一直不持有；当天卖出
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][0] + prices[i] - fee)
    return max(dp[-1])
maxProfit(prices = [1,3,2,8,4,9], fee = 2)