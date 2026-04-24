from typing import List
def maxProfit(k: int, prices: List[int]) -> int:
        dp = [[0 for i in range(1 + 2 * k)] for j in range(len(prices))]
        dp[0][0] = 0
        #第一次持有 1
        #第一次不持有 2
        #第二次持有 3
        #第二次不持有 4

        for i in range(1, 2*k + 1):
            if i % 2:
                dp[0][i] = -prices[0]
            else:
                dp[0][i] = 0
        for i in range(1, len(prices)):
            for j in range(2*k + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif j % 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + prices[i])
        return dp[-1][2*k]
maxProfit(k = 2, prices = [2,4,1])