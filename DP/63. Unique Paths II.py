from typing import List
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    ##起点和终点存在障碍物
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1

    for j in range(cols) :
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

    

    