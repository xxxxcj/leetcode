from queue import Queue

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if root is None:
            return []


        q = Queue()
        ans = []

        q.put(root)
        while not q.empty():
            p = Queue()
            ans.append([])
            while not q.empty():
                node = q.get()
                ans[-1].append(node.val)
                for child in node.children:
                    p.put(child)
            q = p

        return ans