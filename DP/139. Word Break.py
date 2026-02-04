from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            word = s[j:i]
            if word in wordDict and dp[j] == True:
                dp[i] = True
    return dp[len(s)]
# wordBreak(s = "leetcode", wordDict = ["leet","code"])
wordBreak(s="aaaaaaa", wordDict = ["aaaa","aaa"])
    