# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def minus_height(root):
            if root is None:
                return 0
            left_height = minus_height(root.left)
            right_height = minus_height(root.right)
            if left_height == -1 or right_height == -1 or abs(right_height - left_height) > 1:
                return -1
            else:
                return max(right_height, left_height) + 1

        return minus_height(root) >= 0



