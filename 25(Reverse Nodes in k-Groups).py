# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        p = head

        ListNode_len = 0
        while p is not None:
            ListNode_len += 1
            p = p.next
        if ListNode_len < k:
            return head

        prev = None
        curr = head
        tail = head
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        ans = prev

        for i in range(ListNode_len // k - 1):
            prev = None
            tail2 = curr
            for i in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tail.next = prev
            tail = tail2
        tail.next = curr
        return ans


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(3)
x4 = ListNode(4)

x1.next = x2
x2.next = x3
x3.next = x4

ans = Solution().reverseKGroup(x1, 2)

p = ans
while p is not None:
    print(p.val)
    p = p.next
