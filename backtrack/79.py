class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        def dfs(r, c, index):
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            if word[index] != board[r][c]:
                return False
            if index == len(word) - 1: 
                return True
            original = board[r][c]
            board[r][c] = "#"
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            board[r][c] = original
            return found
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False

        