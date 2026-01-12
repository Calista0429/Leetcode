from typing import List
def maximalSquare(matrix: List[List[str]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for i in range(cols + 1)] for i in range(rows + 1)]
    res = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(dp[i][j], res)
    return res * res
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
maximalSquare(matrix)
                
        