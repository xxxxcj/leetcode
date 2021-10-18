# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is not None and root.left is not None:
            p = root
            while p is not None:
                p.left.next = p.right
                if p.next is not None:
                    p.right.next = p.next.left
                p = p.next
            self.connect(root.left)
        return root
