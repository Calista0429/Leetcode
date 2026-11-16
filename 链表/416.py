from typing import List
def canPartition(nums: List[int]) -> bool:
    #这道题是01背包的应用，问的是能否装满容量target的背包
    numSum = sum(nums)
    if numSum % 2 != 0:
        return False
    amount = numSum // 2
    dp = [0] * (amount + 1)
    dp[0] = 0
    for i in range(len(nums)):
        for j in range(amount, nums[i] - 1, -1):
                dp[j] = max(dp[j - nums[i]] + nums[i], dp[j])
    return dp[amount] == amount
canPartition(nums = [1,5,11,5])