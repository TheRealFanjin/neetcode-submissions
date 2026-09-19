class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        bfs = deque()
        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    bfs.append((r, c))
        path_count = 1
        while bfs:
            for _ in range(len(bfs)):
                curr_r, curr_c = bfs.popleft()
                for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r = curr_r + r_dir
                    new_c = curr_c + c_dir
                    if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] > path_count:
                        bfs.append((new_r, new_c))
                        grid[new_r][new_c] = path_count
            path_count += 1
