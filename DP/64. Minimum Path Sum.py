from typing import List
def minPathSum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dp = [[float('inf') for j in range(cols + 1)] for i in range(rows + 1)]
    dp[0][0], dp[1][0], dp[0][1] = 0, 0, 0
   
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dp[i][j] = min(dp[i-1][j] + grid[i - 1][j - 1], dp[i][j-1] + grid[i - 1][j - 1])
    return dp[-1][-1]
minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])