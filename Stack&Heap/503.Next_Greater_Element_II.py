from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    stack = []
    res = [-1] * len(nums)
    for i in range(2 * len(nums)):
        while stack and nums[i % len(nums)] > nums[stack[-1]]:
            idx = stack[-1]
            res[idx] = nums[i % len(nums)]
            stack.pop()
        if i < len(nums):
            stack.append(i)
    return res


# nextGreaterElements(nums = [1,2,1])
# nextGreaterElements(nums = [1,2,3,4,3])
nextGreaterElements(nums = [1,5,3,6,8])
