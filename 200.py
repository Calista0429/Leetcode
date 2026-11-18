from typing import List
def numIslands(grid: List[List[str]]) -> int:
    def dfs(grid, visited, i, j):
        if grid[i][j] == "0":
            return
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited[i][j] = 1
        for d in directions:
            nextx = i + directions[d][0]
            nexty = j + directions[d][1]
            if nextx < 0 or nextx >= rows or nexty < 0 or nextx >= cols:
                continue
            dfs(grid, visited, nextx, nexty)
    
    cols = len(grid[0])
    rows = len(grid)
    visited = [[0] * cols for _ in range(rows)]
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and visited[i][j] == 0:
                res += 1
                visited[i][j] = 1
                dfs(grid, visited, i, j)
    return res
    
numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) 