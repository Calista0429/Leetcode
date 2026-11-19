from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        directions = [(0,1), (1,0), (-1,0), (0, -1)]
        cols = len(grid[0])
        rows = len(grid)
        visited = [[False] * cols for _ in range(rows)]
        
        # def dfs(i, j):
        #     if grid[i][j] == 0:
        #         return 0
        #     visited[i][j] = True
        #     area = 1
        #     for dx, dy in directions:
        #         nextx = i + dx
        #         nexty = j + dy
        #         if nextx < 0 or nextx >= rows or nexty < 0 or nexty >= cols:
        #             continue
        #         if grid[nextx][nexty] == 1 and not visited[nextx][nexty]:
        #             visited[nextx][nexty] = True
        #             area += dfs(nextx, nexty)
        #     return area
        
        def bfs(i, j):
            if grid[i][j] == 0:
                return 0
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            area = 1
            while q:
                curx, cury = q.popleft()
                for dx, dy in directions:
                    nextx = curx + dx
                    nexty = cury + dy
                    if nextx < 0 or nextx >= rows or nexty < 0 or nexty >= cols:
                        continue
                    if grid[nextx][nexty] == 1 and not visited[nextx][nexty]:
                        area += 1
                        q.append((nextx, nexty))
                        visited[nextx][nexty] = True
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    # max_area = max(dfs(i, j), max_area)
                    max_area = max(bfs(i, j), max_area)
        return max_area
        