class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        in_pacific = set()
        in_atlantic = set()

        def dfs(r, c, seen):
            seen.add((r, c))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r + x
                new_c = c + y
                if 0 <= new_r < n and 0 <= new_c < m and (new_r, new_c) not in seen and heights[r][c] <= heights[new_r][new_c]:
                    dfs(new_r, new_c, seen)
        for c in range(m):
            dfs(0, c, in_pacific)
            dfs(n - 1, c, in_atlantic)
        for r in range(n):
            dfs(r, 0, in_pacific)
            dfs(r, m - 1, in_atlantic)
        return [cell for cell in in_pacific if cell in in_atlantic]