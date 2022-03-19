# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        ans = []

        def pre(root: 'Node'):
            if root.children is None:
                return
            for node in root.children:
                pre(node)
            ans.append(root.val)
        if root:
            pre(root)

        return ans