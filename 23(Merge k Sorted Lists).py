# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # ans = ListNode()
        # ans_t = ans
        # l = []
        # for idx, node in enumerate(lists):
        #     if node is None:
        #         l.append(idx)
        # l.reverse()
        # for idx in l:
        #     lists.remove(None)
        # while lists:
        #     min_node = lists[0]
        #     min_idx = 0
        #     for idx, node in enumerate(lists[1:]):
        #         if node.val < min_node.val:
        #             min_node = node
        #             min_idx = idx + 1
        #     ans_t.next = min_node
        #     ans_t = ans_t.next
        #     if min_node.next is None:
        #         lists = lists[:min_idx] + lists[min_idx + 1:]
        #     else:
        #         lists[min_idx] = min_node.next
        # return ans.next
        def merge_two(a: ListNode, b: ListNode):
            ans = ListNode()
            ans_t = ans
            while a is not None and b is not None:
                print(a.val, b.val)
                if a.val < b.val:
                    ans_t.next = a
                    ans_t = ans_t.next
                    a = a.next
                else:
                    ans_t.next = b
                    ans_t = ans_t.next
                    b = b.next
            if a is None:
                ans_t.next = b
            else:
                ans_t.next = a
            return ans.next

        tmp_list1 = lists
        if not tmp_list1:
            return None
        while len(tmp_list1) > 1:
            tmp_list2 = []
            for i in range(0, len(tmp_list1), 2):
                if i + 1 < len(tmp_list1):
                    tmp_list2.append(merge_two(tmp_list1[i], tmp_list1[i + 1]))
                else:
                    tmp_list2.append(tmp_list1[i])
            tmp_list1 = tmp_list2
        return tmp_list1[0]


a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)

print(Solution().mergeKLists([a, b, c]))
