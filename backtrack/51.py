# from typing import List
# def solveNQueens(n: int) -> List[List[str]]:
#         res = []
#         cb = [["." for i in range(n)] for j in range(n)]
#         if not n:
#             return res
#         def backtracking(cb, n, row):
#             if row == n:
#                 res.append(cb[:])
#                 return
#             for i in range(n):
#                 if isValid(cb, n, i, row):
#                     cb[row][i] = "Q"
#                     backtracking(cb, n, row + 1)
#                     cb[row][i] = "."
#         def isValid(cb, n, col, row):
#             for r in range(row, n):
#                 if cb[r][col] == "Q":
#                     return False
#             for c in range(col, n):
#                 if cb[row][c] == "Q":
#                     return False
#             i, j = row - 1, col - 1
#             while i >=0 and j >=0:
#                 if cb[i][j] == "Q":
#                     return False
#                 i -= 1
#                 j -= 1
#             i, j = row -  1, col + 1
#             while i >= 0 and j < n:
#                 if cb[i][j] == "Q":
#                     return False
#                 i -= 1
#                 j += 1
#             return True

                
#         backtracking(cb, n, 0)
#         return res


# solveNQueens(n = 4)
res = [1,5,3,4,6]
print(res == sorted(res))