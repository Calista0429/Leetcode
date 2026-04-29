from typing import List
def findLengthOfLCIS(nums: List[int]) -> int:
    max_len = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] <= nums[j - 1]:
                break
            max_len = max(max_len, j - i + 1)
    return max_len   
findLengthOfLCIS(nums = [1,3,5,4,7])         
    