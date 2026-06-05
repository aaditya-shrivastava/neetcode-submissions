"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        old_head = head
        new_head = head.next
        current_old = old_head
        current_new = new_head
        while current_old:
            current_old.next = current_new.next
            if current_new.next:
                current_new.next = current_new.next.next
            current_old = current_old.next
            current_new = current_new.next
        return new_head