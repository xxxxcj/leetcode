# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = [ListNode(-101, head)]
        while p[0].next is not None:
            if p[0].next.val != p[0].val:
                count = 1
                p2 = [p[0].next]
                while p2[0].next is not None:
                    if p2[0].val == p2[0].next.val:
                        count += 1
                        p2[0] = p2[0].next
                    else:
                        break
                if count >= 2:
                    p[0].next = p2[0].next
                else:
                    p[0] = p[0].next
        return head
