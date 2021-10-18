# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sum_left_leave(root:TreeNode, left:bool):
            if root is None:
                return 0
            if root.right is None and root.left is None and left:
                return root.val
            return sum_left_leave(root.left, True) + sum_left_leave(root.right, False)
        return sum_left_leave(root, False)


x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
print(Solution().sumOfLeftLeaves(x))
