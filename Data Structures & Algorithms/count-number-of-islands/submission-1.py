from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n,m = len(grid), len(grid[0])
        for row in range(n):
            for col in range(m):
                val = grid[row][col]
                if val == "0":
                    continue
                if val == "1":
                    dfs = deque([(row,col)])
                    while dfs:
                        curr_row, curr_col = dfs.popleft()
                        grid[curr_row][curr_col] = "0"
                        if curr_row != 0 and grid[curr_row - 1][curr_col] == "1":
                            dfs.append((curr_row - 1, curr_col))
                        if curr_col != m - 1 and grid[curr_row][curr_col + 1] == "1":
                            dfs.append((curr_row, curr_col + 1))
                        if curr_row != n - 1 and grid[curr_row + 1][curr_col] == "1":
                            dfs.append((curr_row + 1, curr_col))
                        if curr_col != 0 and grid[curr_row][curr_col - 1] == "1":
                            dfs.append((curr_row, curr_col - 1))
                    islands += 1
        return islands