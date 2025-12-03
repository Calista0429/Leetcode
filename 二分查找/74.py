def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0:
            cur_row = cur_col = 0
        else:
            cur_row = mid // rows
            cur_col = mid % cols
        if matrix[cur_row][cur_col] < target:
            left = mid + 1
        elif matrix[cur_row][cur_col] > target:
            right = mid - 1
        else:
            return True
    return False

searchMatrix([[1,1]], 2)