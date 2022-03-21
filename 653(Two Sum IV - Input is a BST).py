# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def search(a: int, root: TreeNode):
            if a == root.val:
                return True
            elif a > root.val:
                if root.right is None:
                    return False
                else:
                    return search(a, root.right)
            else:
                if root.left is None:
                    return False
                else:
                    return search(a, root.left)

        nums = []

        def preorder(root):
            if root is not None:
                preorder(root.left)
                nums.append(root.val)
                preorder(root.right)
        preorder(root)
        for n in nums:
            if search(k - n, root) and k-n != n:
                return True
        return False



