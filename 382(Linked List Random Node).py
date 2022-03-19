# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        p = head
        while p:
            self.vals.append(p.val)
            p = p.next

    def getRandom(self) -> int:
        return random.sample(self.vals, 1)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
