from typing import List
def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for s in strs:
        x = s.count('0')
        y = s.count('1')
        for i in range(m, x - 1, -1):
            for j in range(n, y - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
    return dp[m][n]

strs = ["10","0001","111001","1","0"]
m = 5
n = 3
findMaxForm(strs, m=m, n=n)

    