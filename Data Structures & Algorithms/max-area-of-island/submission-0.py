class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def dfs(coord1, coord2):
            if not (0 <= coord1 < len(grid)) or not (0 <= coord2 < len(grid[0])) or grid[coord1][coord2] == 0:
                return 0
            grid[coord1][coord2] = 0
            return 1 + dfs(coord1 + 1, coord2) + dfs(coord1 - 1, coord2) + dfs(coord1, coord2 + 1) + dfs(coord1, coord2 - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res

