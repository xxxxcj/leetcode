# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        result = []

        def BFS(root, layer=0):
            if len(result) <= layer:
                result.append([])
            if root is not None:
                result[layer].append(root.val)
                BFS(root.left, layer + 1)
                BFS(root.right, layer + 1)

        BFS(root, 0)
        for idx, item in enumerate(result):
            if idx % 2:
                item.reverse()
        return result[:-1]
