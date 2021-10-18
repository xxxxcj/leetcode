class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list:

        ans = []

        if root is None:
            return ans

        def level_order(root, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            if root.left is not None:
                level_order(root.left, level + 1)
            if root.right is not None:
                level_order(root.right, level + 1)

        level_order(root, 0)

        # ans.reverse()

        return ans
