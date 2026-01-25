
from typing_extensions import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [0 for _ in range(target + 1)]
    for num in nums:
        for j in range(target, num - 1, -1):
            if j >= num:
                dp[j] = max(dp[j], dp[j - num] + num)
    return dp[target] == target

nums = [1,2,3,5]
canPartition(nums)