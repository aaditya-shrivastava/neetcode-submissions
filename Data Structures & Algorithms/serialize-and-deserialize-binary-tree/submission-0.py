# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "None"
        queue = collections.deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        while result and result[-1] == "None":
            result.pop()
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "None":
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        i = 1
        while queue and i < len(nodes):
            parent = queue.popleft()
            if nodes[i] != "None":
                left_child = TreeNode(int(nodes[i]))
                parent.left = left_child
                queue.append(left_child)
            i += 1
            if i < len(nodes) and nodes[i] != "None":
                right_child = TreeNode(int(nodes[i]))
                parent.right = right_child
                queue.append(right_child)
            i += 1
        return root