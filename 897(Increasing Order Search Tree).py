# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = TreeNode()

        p = [new_root]

        def preorder(root):
            if root is None:
                return
            preorder(root.left)
            p[0].right = TreeNode(root.val)
            p[0] = p[0].right
            preorder(root.right)

        preorder(root)

        return new_root.right