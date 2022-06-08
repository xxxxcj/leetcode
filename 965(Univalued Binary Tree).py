# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def is_same(root: TreeNode, root_value):
            if root.val != root_value:
                return False
            if root is None:
                return True
            return is_same(root.left, root_value) and is_same(root.right, root_value)
        return is_same(root, root.val)