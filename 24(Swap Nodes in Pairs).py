# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode):
        if head is not None and head.next is not None:
            ans = head.next
            tmp = head.next.next
            head.next.next = head
            head.next = tmp
            p1 = head
            p2 = head.next
            p3 = p2.next if p2 is not None else None
        else:
            ans = head
            return ans
        while p2 is not None and p3 is not None:
            p1.next = p3
            tmp = p3.next
            p3.next = p2
            p2.next = tmp
            if p2.next is not None:
                p1 = p2
                p2 = p1.next
                p3 = p2.next
            else:
                return ans
        return ans


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(3)
x4 = ListNode(4)

x1.next = x2
x2.next = x3
x3.next = x4


ans = Solution().swapPairs(x1)
p = ans
while p is not None:
    print(p.val)
    p = p.next
