# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        sorted_list = []

        def get_sorted_list(root):
            if root is None:
                return
            get_sorted_list(root.left)
            sorted_list.append(root.val)
            get_sorted_list(root.right)

        get_sorted_list(root)

        min_abs_diff = float('inf')
        for i in range(1, len(sorted_list)):
            if min_abs_diff > abs(sorted_list[i-1] - sorted_list[i]):
                min_abs_diff = abs(sorted_list[i-1] - sorted_list[i])
        return min_abs_diff
