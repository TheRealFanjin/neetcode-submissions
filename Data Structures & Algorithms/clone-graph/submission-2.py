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
            return
        node_hashmap = {node: Node(node.val)}
        bfs = deque([node])
        while bfs:
            curr = bfs.popleft()
            if curr not in node_hashmap:
                node_hashmap[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in node_hashmap:
                    node_hashmap[neighbor] = Node(neighbor.val)
                    bfs.append(neighbor)
                node_hashmap[curr].neighbors.append(node_hashmap[neighbor])

        return node_hashmap[node]