class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        threeSet = [set(), set(), set()]
        for rowCount, row in enumerate(board):
            rowSet = set()
            for colCount, column in enumerate(row):
                if column != '.':
                    if column in rowSet or int(column) > 9 or int(column) < 1:
                        print('s')
                        return False
                    rowSet.add(column)
                
                    if column in colSet[colCount]:
                        print('a')
                        return False
                    colSet[colCount].add(column)

                    if colCount < 3:
                        if column in threeSet[0]:
                            print('b', column, rowCount, colCount)
                            print(threeSet[0])

                            return False
                        else:
                            threeSet[0].add(column)
                    elif colCount < 6:
                        if column in threeSet[1]:
                            print('c')
                            return False
                        else:
                            threeSet[1].add(column)
                    else:
                        if column in threeSet[2]:
                            print('d')
                            return False
                        else:
                            threeSet[2].add(column)
                    
            if rowCount == 2 or rowCount == 5:
                threeSet = [set(), set(), set()]

        return True