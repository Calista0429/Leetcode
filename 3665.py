from functools import cache
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        MOD = 10**9 + 7
        cols = len(grid[0])
        rows = len(grid)
        @cache
        def dfs(i: int , j: int, k: int) -> int:
            # k = 0: 向下
            # k = 1: 向右
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0
            if i == rows - 1 and j == cols - 1:
                return 1
            if grid[i][j] == 0:
                return (dfs(i + 1, j, 0) + dfs(i, j + 1, 1)) % MOD
            # if grid[i][j] == 1 and k == 1:
            #     return dfs(i + 1, j, 0)
            if k == 1:
                return dfs(i + 1, j, 0)
            # if grid[i][j] == 1 and k == 0:            
            #     return dfs(i, j + 1, 1)
            return dfs(i, j + 1, 1)
        res = dfs(0, 0, 0)
        # dfs.cache_clear()
        dfs.cache_clear()
        return res


    
        

