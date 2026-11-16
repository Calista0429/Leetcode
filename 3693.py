from typing import List
def climbStairs(n: int, costs: List[int]) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        jump1, jump2, jump3 = float('inf'),float('inf'),float('inf')
        if i + 1 < len(costs):
            jump1 = costs[i + 1] + 1
        if i + 2 < len(costs):
            jump2 = costs[i + 2] + 4
        if i + 3 < len(costs):
            jump3 = costs[i + 3] + 9
        dp[i] = min(dp[i], jump1, jump2, jump3)
    return dp[n]
climbStairs(4)