def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    prefix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= prefix
        prefix *= nums[i]
    
    return res
nums = [1,2,3,4]
productExceptSelf(nums)