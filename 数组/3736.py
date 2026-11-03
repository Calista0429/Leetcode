class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        res = 0
        for num in nums:
            res += abs(num - max_num)
        return res

        
