class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l,row_r = 0, len(matrix) - 1
        while row_l <= row_r:
            row_mid = row_l + (row_r - row_l) // 2
            if matrix[row_mid][0] == target or matrix[row_mid][-1] == target:
                return True
            if matrix[row_mid][0] < target < matrix[row_mid][-1]:
                col_l,col_r = 0, len(matrix[0]) - 1
                while col_l <= col_r:
                    print(row_mid, col_l, col_r)
                    col_mid = col_l + (col_r - col_l) // 2
                    if matrix[row_mid][col_l] == target or matrix[row_mid][col_r] == target or matrix[row_mid][col_mid] == target:
                        return True
                    if target > matrix[row_mid][col_mid]:
                        col_l = col_mid + 1
                        col_r -= 1
                    else:
                        col_r = col_mid - 1
                        col_l += 1
                return False
            elif target > matrix[row_mid][-1]:
                row_l = row_mid + 1
            elif target < matrix[row_mid][0]:
                row_r = row_mid - 1
        return False
            