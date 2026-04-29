from typing import List
def lengthOfLIS(nums: List[int]) -> int:
    #以nums[i]为结尾的最长子序列长度dp[i]
    dp = [1 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        # if nums[i] > nums[i - 1]:
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)
lengthOfLIS(nums = [0,1,0,3,2,3])