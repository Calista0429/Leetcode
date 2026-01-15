from typing import List
def maxProduct(nums: List[int]) -> int:
    dp_max = [0 for _ in range(len(nums))]
    dp_min = [0 for _ in range(len(nums))]
    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    for i in range(1, len(nums)):
        dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
    return max(dp_max)