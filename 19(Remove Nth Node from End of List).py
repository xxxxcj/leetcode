# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        '''
        # 第一印象，扫描一次获得长度，然后确定删除哪个节点
        list_length = 0
        p = head
        # 计算链表长度
        while p is not None:
            p = p.next
            list_length += 1

        i = 0
        p = head
        while p is not None:
            if n == list_length:
                head = p.next
                break
            elif i + n == list_length - 1:
                p.next = p.next.next
                break
            p = p.next
            i += 1
        return head
        '''

        # 双指针法
        p1, p2 = head, head
        i = 0
        while p2.next is not None:
            if i < n:
                p2 = p2.next
                i += 1
            else:
                p1 = p1.next
                p2 = p2.next
        # print(p1.val, p2.val, i, n)
        if i < n:
            head = p1.next
        else:
            p1.next = p1.next.next
        return head


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(3)
x4 = ListNode(4)
x5 = ListNode(5)

x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5

head = x1
ans = Solution().removeNthFromEnd(head, 3)
p = ans
while p is not None:
    print(p.val)
    p = p.next
