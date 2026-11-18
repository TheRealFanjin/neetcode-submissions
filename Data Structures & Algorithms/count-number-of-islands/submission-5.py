class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs = deque([(i, j)])
                    grid[i][j] = '0'
                    while bfs:
                        curr_r, curr_c = bfs.popleft()
                        for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_r = curr_r + r_dir
                            new_c = curr_c + c_dir
                            if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == '1':
                                bfs.append((new_r, new_c))
                                grid[new_r][new_c] = '0'
                    islands += 1
        return islands