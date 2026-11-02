class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        left, right = 0, n - 1
        res = 0
        while left < right:
            res = res + nums[right] - nums[left]
            left += 1
            right -= 1
        return res

        
