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
        old_to_new = {}
        queue = [node]
        old_to_new[node] = Node(node.val)
        while queue:
            current_original = queue.pop(0)
            current_cloned = old_to_new[current_original]
            for neighbor_original in current_original.neighbors:
                if neighbor_original not in old_to_new:
                    old_to_new[neighbor_original] = Node(neighbor_original.val)
                    queue.append(neighbor_original)
                current_cloned.neighbors.append(old_to_new[neighbor_original])
        return old_to_new[node]