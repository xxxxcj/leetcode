# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 常规想到的非递归法
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        #
        # p1, p2 = l1, l2
        # if p1.val > p2.val:
        #     ans = p2
        #     p2 = p2.next
        # else:
        #     ans = p1
        #     p1 = p1.next
        #
        # p = ans
        # while p1 is not None and p2 is not None:
        #     if p1.val > p2.val:
        #         p.next = p2
        #         p = p.next
        #         p2 = p2.next
        #     else:
        #         p.next = p1
        #         p = p.next
        #         p1 = p1.next
        #
        # if p1 is None:
        #     p.next = p2
        # else:
        #     p.next = p1
        #
        # return ans

        # 递归法
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(4)

x1.next = x2
x2.next = x3

y1 = ListNode(1)
y2 = ListNode(3)
y3 = ListNode(4)

y1.next = y2
y2.next = y3

ans = Solution().mergeTwoLists(x1, y1)
p = ans
while p is not None:
    print(p.val)
    p = p.next
