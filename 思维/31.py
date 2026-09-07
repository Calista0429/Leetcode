from typing import List
def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1, -1, -1):
        if i + 1 < len(nums) and nums[i] < nums[i + 1]:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
            break
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left] 
        left += 1
        right -=1

# a = [3,5,4,2,1]
nextPermutation([3,2,1])
# print(sorted(a, reverse=True))