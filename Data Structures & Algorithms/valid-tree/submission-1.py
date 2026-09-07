class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = {0}
        def dfs(node, parent):
            nonlocal visited
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
