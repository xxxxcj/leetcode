# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def find_tilt(root: TreeNode):
            if root is None:
                return 0, 0
            val_left_tree, tilt_left = find_tilt(root.left)
            val_right_tree, tilt_right = find_tilt(root.right)
            return val_left_tree + val_right_tree + root.val, tilt_left + tilt_right + abs(
                val_left_tree - val_right_tree)

        _, val = find_tilt(root)
        return val
