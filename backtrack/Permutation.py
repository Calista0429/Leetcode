class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def backtracking(nums):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(nums)
                    path.pop()
        backtracking(nums)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))  # Example usage