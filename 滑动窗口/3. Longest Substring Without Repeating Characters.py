def lengthOfLongestSubstring(s):
    max_length = 0
    left = 0
    res = set()
    for right in range(len(s)):
        while s[right] in res:
            res.remove(s[left])
            left += 1
        res.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

s = "pwwkew"
lengthOfLongestSubstring(s)



        