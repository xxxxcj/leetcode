# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.i = 0

        def preorder(root):
            if root.left is not None:
                preorder(root.left)
            self.stk.append(root.val)
            if root.right is not None:
                preorder(root.right)

        preorder(root)

    def next(self) -> int:
        self.i += 1
        return self.stk[self.i-1]

    def hasNext(self) -> bool:
        if self.i < len(self.stk):
            return True
        return False




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()