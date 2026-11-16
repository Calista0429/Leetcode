def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_len = 0
    for num in nums:
        if num - 1 in nums:
            continue
        length = 1
        while num + 1 in nums:
            length += 1
        max_len = max(max_len, length)
    return max_len
longestConsecutive(nums = [100,4,200,1,3,2])