class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #时间复杂度 o(mxn) 空间复杂度 o(1)
        midx = m - 1
        nidx = n - 1
        right = m + n - 1
        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            right -= 1

        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()
            

###这段代码是使用快慢指针双指针对两个数组中最大的来进行遍历

        
        