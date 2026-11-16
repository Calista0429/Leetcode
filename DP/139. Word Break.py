# from typing import List
# def wordBreak(s: str, wordDict: List[str]) -> bool:
#     dp = [False for _ in range(len(s) + 1)]
#     dp[0] = True
#     for i in range(1, len(s) + 1):
#         for j in range(i):
#             word = s[j:i]
#             if word in wordDict and dp[j] == True:
#                 dp[i] = True
#     return dp[len(s)]

#优化解法
#优化思路：1.将原本wordDict列表改成哈希表，这样word in wordDict只需要O(1)复杂度
#         2. 使用最大长度窗口，保证s[j:i]的长度不会超过wordDict中最长的字符串
#         3. 将dp[j] = True放在了if else的左边，因为在判断的时候是从左往右的。
def wordBreak(s: str, wordDict: list[str]) -> bool:
    #这里的dp含义是，长度为i的字符串，能够被合法地拆分
    words = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    max_len = max(len(word) for word in words)
    for i in range(1, len(s) + 1):
        for j in range(max(i - max_len, 0), i):
            #dp[0:i] = dp[0:j] + dp[j:i]
            #根据dp的含义，如果dp[i]能够被拆分，需要dp[j]首先能够被拆分
            word = s[j:i]
            if dp[j] == True and  word in words:
                dp[i] = True
                break
    return dp[len(s)]

wordBreak(s = "leetcode", wordDict = ["leet","code"])
# wordBreak(s="aaaaaaa", wordDict = ["aaaa","aaa"])
    