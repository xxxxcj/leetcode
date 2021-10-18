# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = [head]
        while p[0].next is not None:
            if p[0].val == p[0].next.val:
                p[0].next = p[0].next.next
            else:
                p[0] = p[0].next
        return head