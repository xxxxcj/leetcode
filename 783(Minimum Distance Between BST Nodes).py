# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ret = list()

        def pre_traverse(root):
            if root.left is not None:
                pre_traverse(root.left)
            ret.append(root.val)
            if root.right is not None:
                pre_traverse(root.right)

        pre_traverse(root)

        min = ret[1] - ret[0]
        for i in range(2, len(ret)):
            if min > ret[i] - ret[i - 1]:
                min = ret[i] - ret[i - 1]

        return min