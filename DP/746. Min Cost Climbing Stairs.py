from typing import List
def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [float('inf') for _ in range(len(cost))]
    dp[0] = dp[1] = 0
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return min(dp[-1], dp[-2])
cost = [10,15,20]
minCostClimbingStairs(cost)