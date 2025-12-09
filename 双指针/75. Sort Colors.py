def sortColors(self, nums):
    
    for right in range(len(nums) - 1, -1 , -1):
        left  =  0
        while left <= right:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums