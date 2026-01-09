from typing import List
def findLength(nums1: List[int], nums2: List[int]) -> int:
    dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
    res = 0
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            res = max(dp[i][j], res)
    return res

nums1 = [1,1,0,0,1,1]
nums2 = [0,0]
findLength(nums1, nums2)