class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = deque()
        minutes = 0
        n, m = len(grid), len(grid[0])
        fresh_fruits = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    bfs.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1
        while bfs:
            for _ in range(len(bfs)):
                curr_r, curr_c = bfs.popleft()
                for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r = curr_r + r_dir
                    new_c = curr_c + c_dir
                    if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        bfs.append((new_r, new_c))
                        fresh_fruits -= 1
            if bfs:
                minutes += 1
        return minutes if not fresh_fruits else -1
            