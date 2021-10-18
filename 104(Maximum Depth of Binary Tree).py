# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def max_depth(root: TreeNode):
            left_depth, right_depth = 1, 1
            if root.left is not None:
                left_depth = 1 + max_depth(root.left)
            if root.right is not None:
                right_depth = 1 + max_depth(root.right)
            return max(left_depth, right_depth)
        return max_depth(root)