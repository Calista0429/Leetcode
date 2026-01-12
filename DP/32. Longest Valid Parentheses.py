def longestValidParentheses(s: str) -> int:
    if not s:
        return 0
    dp = [0 for _ in range(len(s))]
    res = 0
    for i in range(1, len(s)):
        if s[i] == "(":
            continue
        else:
            if s[i - 1] == "(":
                if i >= 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            elif s[i - 1] == ")":
                j = i - dp[i - 1] - 1
                if j >= 0 and s[j] == "(":
                    if j >= 1:
                        dp[i] = dp[i - 1] + dp[j - 1] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
    return max(dp)


        