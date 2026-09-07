class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        bfs_q = deque()
        traversed = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs_q.append((i, j))
                    traversed.add((i, j))
        distance = 0
        while bfs_q:
            for _ in range(len(bfs_q)):
                coord1, coord2 = bfs_q.popleft()
                grid[coord1][coord2] = distance
                for dir1 in dirs:
                    new_coord1, new_coord2 = coord1 + dir1[0], coord2 + dir1[1]
                    if (new_coord1, new_coord2) not in traversed and 0 <= new_coord1 < n and 0 <= new_coord2 < m and grid[new_coord1][new_coord2] != -1:
                        bfs_q.append((new_coord1, new_coord2))
                        traversed.add((new_coord1, new_coord2))
            distance += 1
                        
            