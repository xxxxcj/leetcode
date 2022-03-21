# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""

        def preorder(root: TreeNode):
            nonlocal ans
            ans = ans + str(root.val)
            if root.left is not None:
                ans += '('
                preorder(root.left)
                ans += ')'
            if root.left is None and root.right is not None:
                ans += '()'
            if root.right is not None:
                ans += '('
                preorder(root.right)
                ans += ')'

        preorder(root)
        return ans
