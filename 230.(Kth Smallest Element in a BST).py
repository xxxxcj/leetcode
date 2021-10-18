# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val_list = list()

        def mid_traversal(root: TreeNode):
            if root.left is not None:
                mid_traversal(root.left)
            val_list.append(root.val)
            if root.right is not None:
                mid_traversal(root.right)

        mid_traversal(root)

        return val_list[k-1]