class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = deque()
        n = len(grid)
        m = len(grid[0])
        total_fresh = 0
        visited = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    bfs.append((r, c))
                    total_fresh += 1
                elif grid[r][c] == 1:
                    total_fresh += 1
        minutes = 0
        rotted = 0
        while bfs:
            print(bfs, minutes)
            for _ in range(len(bfs)):
                r, c = bfs.popleft()
                rotted += 1
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r = r + x
                    new_c = c + y
                    if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        bfs.append((new_r, new_c))
            if bfs:
                minutes += 1
        print(rotted, total_fresh)
        return minutes if rotted == total_fresh else -1