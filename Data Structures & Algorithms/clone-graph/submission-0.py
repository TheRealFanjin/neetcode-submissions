"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_map = {}
        processed = set()
        bfs_q = deque([node])
        while bfs_q:
            curr_node = bfs_q.popleft()
            if curr_node in processed:
                continue
            processed.add(curr_node)
            if curr_node not in node_map:
                node_map[curr_node] = Node(curr_node.val)
            for neighbor in curr_node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                node_map[curr_node].neighbors.append(node_map[neighbor])
                bfs_q.append(neighbor)
        return node_map[node]
            