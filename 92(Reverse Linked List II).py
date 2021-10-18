# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        i = 0
        new_head = ListNode(-1, head)
        p = new_head
        left_end = p
        p_next = p.next
        p_last = None
        while i <= right:
            if i == left - 1:
                left_end = p
            if i > left:
                p.next = p_last

            p_last = p
            p = p_next
            if p is not None:
                p_next = p.next
            i += 1

        tmp = left_end.next
        left_end.next = p_last
        tmp.next = p

        return head.next