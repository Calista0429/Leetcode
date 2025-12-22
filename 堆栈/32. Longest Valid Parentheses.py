def longestValidParentheses(s: str) -> int:
    if not s:
        return 0
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                length = i - stack[-1]
                max_len = max(length, max_len)
            else:
                stack.append(i)
    return max_len

# longestValidParentheses(s = "(()")
# longestValidParentheses(s = ")()())")
longestValidParentheses(s=")))))(((((")

    
    