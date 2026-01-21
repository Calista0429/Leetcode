from typing import List
def maxSubArray(self, nums: List[int]) -> int:
    res, count = float('-inf'), 0
    for i in range(len(nums)):
        count += nums[i]
        res = max(res, count)
        if count < 0:
            count = 0 
    return res

    