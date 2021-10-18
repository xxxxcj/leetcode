# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:

        ans = []

        if root is None:
            return ans

        def level_order_bottom(root, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            if root.left is not None:
                level_order_bottom(root.left, level + 1)
            if root.right is not None:
                level_order_bottom(root.right, level + 1)

        level_order_bottom(root, 0)

        ans.reverse()

        return ans


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
print(Solution().levelOrderBottom(root))
