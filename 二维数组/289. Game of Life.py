


def count_neighbour(i, j, board, rows, cols):
    live_count = 0
    if i - 1 >= 0:
        live_count += board[i - 1][j]
    if j - 1 >= 0:
        live_count += board[i - 1][j - 1]
    if j + 1 <= cols:
        live_count += board[i - 1][j + 1]
    if i + 1 <= rows:
        live_count += board[i + 1][j]
        if j - 1 >= 0:
            live_count += board[i + 1][j - 1]
        if j + 1 <= cols:
            live_count += board[i + 1][j + 1]
    if j - 1 >= 0:
        live_count += board[i][j - 1]
    if j + 1 <= cols:
        live_count += board[i][j + 1]
    return live_count

    

def gameOfLife(board):
    count = 0
    rows = len(board) - 1
    cols = len(board[0]) - 1
    res = []
    for i in range(rows + 1):
        layer = []
        for j in range(cols + 1):
            layer.append(board[i][j])
        res.append(layer)
        
    for i in range(rows + 1):
        for j in range(cols + 1):
            if res[i][j] == 0:
                count = count_neighbour(i, j, res, rows, cols)
                # print(count)
                # break
                if count == 3:
                    board[i][j] = 1
            else:
                count = count_neighbour(i, j, res, rows, cols)
                if count < 2:
                    board[i][j] = 0
                elif count == 2 or count == 3:
                    board[i][j] = 1
                elif count > 3:
                    board[i][j] = 0   
    return board

board =[[1,1]]
gameOfLife(board)