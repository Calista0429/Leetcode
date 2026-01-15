from typing import List
def rob(nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]

def get_max(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))


    