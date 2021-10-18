# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        head_ptr = []
        p = head
        length = 0
        while p is not None:
            head_ptr.append(p)
            length += 1
            p = p.next

        k %= length
        new_head = head_ptr[-k]
        head_ptr[-1].next = head
        head_ptr[-k - 1].next = None
        return new_head


val_list = [1, 2, 3, 4, 5]
head = ListNode(val_list[0])
p = head
for val in val_list[1:]:
    p.next = ListNode(val)
    p = p.next
k = 15
t = Solution().rotateRight(head, k)
while t is not None:
    print(t.val)
    t = t.next
