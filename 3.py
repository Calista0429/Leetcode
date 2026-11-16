def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    visit = set()
    left, right = 0, 0
    # for right in range(len(s)):
    #     while s[right] in visit:
    #         visit.remove(s[left])
    #         left += 1
    #     visit.add(s[right])
    #     max_len = max(max_len, right - left + 1)
    # return max_len
    while left >= 0 and right < len(s):
        substr = s[left: right]
        if s[right] in substr:
            left += 1
        else:
            right += 1
        max_len = max(max_len, right - left)
    return max_len
lengthOfLongestSubstring(s = "abcabcbb")           
    
        

    