class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []
        n, m = len(heights), len(heights[0])
        for c in range(m):
            pacific.add((0, c))
            atlantic.add((n - 1, c))
        for r in range(n):
            pacific.add((r, 0))
            atlantic.add((r, m - 1))
        pacific_dfs = list(pacific)
        while pacific_dfs:
            curr_r, curr_c = pacific_dfs.pop()
            for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r_dir + curr_r
                new_c = c_dir + curr_c
                if 0 <= new_r < n and 0 <= new_c < m and heights[new_r][new_c] >= heights[curr_r][curr_c] and (new_r, new_c) not in pacific:
                    pacific_dfs.append((new_r, new_c))
                    pacific.add((new_r, new_c))
        atlantic_dfs = list(atlantic)
        visited = set(atlantic)
        while atlantic_dfs:
            curr_r, curr_c = atlantic_dfs.pop()
            if (curr_r, curr_c) in pacific:
                res.append([curr_r, curr_c])
            for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r_dir + curr_r
                new_c = c_dir + curr_c
                if 0 <= new_r < n and 0 <= new_c < m and heights[new_r][new_c] >= heights[curr_r][curr_c] and (new_r, new_c) not in visited:
                    atlantic_dfs.append((new_r, new_c))
                    visited.add((new_r, new_c))
        return res
        
