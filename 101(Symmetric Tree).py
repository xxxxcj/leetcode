# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        def Symmetric(left: TreeNode, right: TreeNode):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val == right.val:
                return Symmetric(left.right, right.left) and Symmetric(left.left, right.right)
            else:
                return False
        return Symmetric(root.left, root.right)
