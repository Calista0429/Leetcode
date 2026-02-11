from typing import List
def maxProfit(prices: List[int]) -> int:
    dp = [[0 for i in range(4)] for j in range(len(prices))]
    #持有股票
    dp[0][0] = -prices[0]
    #持续不持有
    dp[0][1] = 0
    #当天卖出股票
    dp[0][2] = 0
    #冷冻期
    dp[0][3] = 0
    for i in range(1, len(prices)):
        #持有股票（一直持有；当天持有; 冷冻期后一天持有）
        dp[i][0] = max(dp[i - 1][0], 
                        dp[i - 1][1] - prices[i], 
                        dp[i - 1][3] - prices[i])
        #持续不持有（冷冻期后一天不持有；冷冻期之后连续不持有）
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
        #当天买出(前一天是持有的状态，然后卖出)
        dp[i][2] = dp[i - 1][0] + prices[i]
        #冷冻期(前一天一定是卖出的状态)
        dp[i][3] = dp[i - 1][2]
    return max(dp[-1])
    