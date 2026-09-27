class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for (edge1, edge2) in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        bfs = deque([0])
        visited = set(bfs)
        while bfs:
            curr = bfs.popleft()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    bfs.append(neighbor)
                    visited.add(neighbor)
        return len(visited) == n