class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = [set() for i in range(9)]
        square_set = [set() for i in range(3)]

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".":
                    continue
                # row check
                if number in row_set:
                    print('row_false')
                    return False
                else:
                    row_set.add(number)
                # col check
                if number in col_set[j]:
                    print('col_false')
                    return False
                else:
                    col_set[j].add(number)
                #square check
                if 0 <= j < 3:
                    if number in square_set[0]:
                        return False
                    else:
                        square_set[0].add(number)
                elif 3 <= j < 6:
                    if number in square_set[1]:
                        return False
                    else:
                        square_set[1].add(number)
                elif 6 <= j < 9:
                    if number in square_set[2]:
                        return False
                    else:
                        square_set[2].add(number)
            row_set = set()
            if i in [2, 5, 8]:
                square_set = [set() for i in range(3)]
        return True