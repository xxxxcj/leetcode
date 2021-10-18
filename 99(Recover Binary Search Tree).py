# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        bst_list = []

        def change_tree_to_list(root: TreeNode):
            if root is not None:
                change_tree_to_list(root.left)
                bst_list.append(root.val)
                root.val = None
                change_tree_to_list(root.right)

        def put_into_tree(root: TreeNode):
            if root is not None:
                put_into_tree(root.left)
                root.val = bst_list[-1]
                bst_list.pop()
                put_into_tree(root.right)

        change_tree_to_list(root)
        bst_list.sort(reverse=True)
        put_into_tree(root)


def printTree(root: TreeNode):
    if root is not None:
        printTree(root.left)
        print(root.val)
        root.val = None
        printTree(root.right)


root = TreeNode()
root.val = 1
root.left = TreeNode()
root.left.val = 3
root.left.right = TreeNode()
root.left.right.val = 2
Solution().recoverTree(root)
printTree(root)




