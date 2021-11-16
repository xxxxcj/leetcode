# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        p_next = node.next

        while p_next.next is not None:
            p.val = p_next.val
            p = p_next
            p_next = p_next.next

        p.val = p_next.val
        p.next = None
