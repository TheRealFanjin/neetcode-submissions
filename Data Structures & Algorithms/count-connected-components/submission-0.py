class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        res = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            bfs_q = deque([i])
            while bfs_q:
                node = bfs_q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        bfs_q.append(neighbor)
            res += 1
        return res
