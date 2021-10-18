# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = [0]

        def preorder(root):
            if root is None:
                return
            preorder(root.left)
            if low <= root.val <= high:
                result[0] += root.val
            preorder(root.right)

        preorder(root)

        return result

