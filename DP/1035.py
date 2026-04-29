from typing import List
def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    # dp = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    print((dp))
    # res = 0
    # for i in range(1, len(nums1) + 1):
    #     for j in range(1, len(nums2) + 1):
    #         if nums1[i - 1] == nums2[j - 1]:
    #             dp[i][j] = dp[i - 1][j - 1] + 1
    #         else:
    #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    #         res = max(res, dp[i][j])
    # return res
    

maxUncrossedLines(nums1 = [1,4,2], nums2 = [1,2,4])