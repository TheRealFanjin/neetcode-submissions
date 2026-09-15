class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs = [(r, c)]
                    grid[r][c] == '0'
                    while dfs:
                        curr_r, curr_c = dfs.pop()
                        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_r = curr_r + direction[0] 
                            new_c = curr_c + direction[1]
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == '1':
                                dfs.append((new_r, new_c))
                                grid[new_r][new_c] = '0'
                    count += 1
        return count