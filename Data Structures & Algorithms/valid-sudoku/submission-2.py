class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sqr_set = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val in row_set[row] or val in col_set[col] or val in sqr_set[3 * (row // 3) + col // 3]:
                    return False
                row_set[row].add(val)
                col_set[col].add(val)
                sqr_set[3 * (row // 3) + col // 3].add(val)
        return True