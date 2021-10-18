# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0  # 进位
        result = ListNode(0)  #头节点
        p = result
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            val = x + y + carry
            p.next = ListNode(val % 10)
            carry = val // 10  # 通过除法取高位效率比判断更高 carry = 1 if val > 9 else 0
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            p.next = ListNode(carry)
        return result.next
