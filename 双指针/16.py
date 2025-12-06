nums = [-1,2,1,-4]
target = 1
res = 0
def threeSumClosest(nums, target):
    nums.sort()
    diff = 9999999
    for i in range(len(nums)):
        if nums[i - 1] == nums[i]:
            continue

        j = i
        k = len(nums) - 1
        
        while j < k:        
            total = nums[i] + nums[j] + nums[k]
            if abs(target - total) < diff:
                diff = abs(target - total)
                res = total
            j += 1
            while nums[j - 1] == nums[j] and j < k:
                j += 1
    return res

threeSumClosest(nums, target)