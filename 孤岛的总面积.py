###计算海洋中的孤岛面积
###孤岛的定义是：四周都是海洋，不能触碰到边缘

### 思路是先将海洋中靠岸的陆地, 通过dfs都置为0
### 然后统计一下1的数量就是孤岛的面积

def lonelyIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def dfs(i,j):
        grid[i][j] = 0
        for dx, dy in direction:
            nextx = i + dx
            nexty = j + dy
            if nextx < 0 or nextx >= rows or nexty < 0 or nexty >= cols:
                continue
            if grid[nextx][nexty] == 1:
                dfs(nextx, nexty)

    for i in range(rows):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][cols - 1] == 1:
            dfs(i, cols - 1)

    for j in range(cols):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[rows - 1][j] == 1:
            dfs(rows - 1, j)
    print(grid)
    res = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1): 
            if grid[i][j] == 1:
                res += 1
    # return res
    print(res)
lonelyIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])