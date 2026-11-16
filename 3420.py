from typing import List
def countNonDecreasingSubarrays(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    n = len(nums)
    total = (1 + n) * n // 2
    left, right = 0, 1
    count = 0
    while left < right and right < len(nums):
        subarr = nums[left: right + 1]
        max_num = max(subarr)
        step = 0
        for num in subarr:
            if num != max_num:
                step += max_num - num
        if step > k:
            left += 1
            count += n - right
            right = left + 1
        elif right == len(nums) - 1:
            left += 1
            right = left + 1
        else:
            right += 1
        print(left, right)
    print(total - count)
    return total - count


# countNonDecreasingSubarrays(nums = [6,3,1,2,4,4], k = 7)
countNonDecreasingSubarrays(nums = [6,3,1,3,6], k = 4)

