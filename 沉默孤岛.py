def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = len(board)
    cols = len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0,1), (1,0), (-1, 0), (0, -1)]

    def dfs(visited, i, j):
        visited[i][j] = True
        for dx, dy in directions:
            nextx = i + dx
            nexty = j + dy
            if nextx < 0 or nextx >= rows or nexty < 0 or nexty >= cols:
                continue
            if board[nextx][nexty] == "O" and not visited[nextx][nexty]:
                visited[nextx][nexty] = True
                dfs(visited, nextx, nexty)
            
    for i in range(rows):
        if board[i][0] == "O":
            visited[i][0] = True
            dfs(visited, i, 0)
        if board[i][cols - 1] == "O":
            visited[i][cols - 1] = True
            dfs(visited, i, cols - 1)
    for j in range(cols):
        if board[0][j] == "O":
            visited[0][j] = True
            dfs(visited, 0, j)

        if board[rows - 1][j] == "O":
            visited[rows - 1][j] = True 
            dfs(visited, rows - 1, j)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if board[i][j] == "O" and not visited[i][j]:
                board[i][j] = "X"
    
    for i in range(rows):
        print(board[i][:])
    # print(visited[i][:])
solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])



[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]


[False, False, True, False, False, False, False, True, False, False, False, False, False]
[False, False, False, False, False, False, False, True, True, True, False, False, False]
[False, True, True, False, True, False, False, False, False, False, False, False, False]
[False, True, False, False, True, True, False, False, True, False, True, False, False]
[False, True, False, False, True, True, False, False, True, True, True, False, False]
[False, False, False, False, False, False, False, False, False, False, True, False, False]
[False, False, False, False, False, False, False, True, True, True, False, False, False]
[False, False, False, False, False, False, False, True, True, False, False, False, False]