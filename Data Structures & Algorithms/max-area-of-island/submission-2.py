"""
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs = [(r, c)]
                    grid[r][c] = 0
                    curr_area = 0
                    while dfs:
                        curr_r, curr_c = dfs.pop()
                        curr_area += 1
                        for (dir1, dir2) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_r, new_c = curr_r + dir1, curr_c + dir2
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                                grid[new_r][new_c] = 0
                                dfs.append((new_r, new_c))
                    max_area = max(max_area, curr_area)
        return max_area