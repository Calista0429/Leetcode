from collections import deque
from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    cols = len(grid[0])
    rows = len(grid)
    fresh = 0
    time = 0
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                r += dr
                c += dc
                if (r >= rows or r < 0) or (c >= cols or c < 0) or grid[r][c] != 1:
                    continue
                grid[r][c] = 2
                q.append([r, c])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1

orangesRotting([[1,2]])
                
    