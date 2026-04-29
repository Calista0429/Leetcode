def countSubstrings(s: str) -> int:
    #[i,j]的子串中有多少个回文子串
    dp = [[False] * (len(s)) for _ in range(len(s))]
    res = 0
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                #j-i=1: aa,bb,cc这种类型
                #j-i=0: a, b, c这种类型
                if j - i <= 1:
                    dp[i][j] = True
                    res += 1                      
                elif dp[i + 1][j - 1]:
                    #如果[i, i+1,..., j-1, j]中的[i + 1, j - 1]之间是回文串
                    dp[i][j] = True
                    res += 1
                # res += 1
    return res
countSubstrings("aaa")
                    
                
        

    