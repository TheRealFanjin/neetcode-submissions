"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap = {node: Node(node.val)}
        bfs = deque([node])
        while bfs:
            original_node = bfs.popleft()
            for neighbor in original_node.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                    bfs.append(neighbor)
                hashmap[original_node].neighbors.append(hashmap[neighbor])
        return hashmap[node]