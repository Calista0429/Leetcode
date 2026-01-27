from typing import List
def findTargetSumWays(nums: List[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 != 0:
        return 0
    left = (total + target) // 2
    dp = [0 for _ in range(total + 1)]
    dp[0] = 1
    for num in nums:
        for j in range(left, num - 1, -1):
            dp[j] += dp[j - num] + num
    return dp[left]

findTargetSumWays(nums = [1,1,1,1,1], target = 3)