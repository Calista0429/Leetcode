from typing import List
def rob(nums: List[int]) -> int:
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return max(dp)
