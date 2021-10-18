# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        linklist_val = []
        for i in lists:
            linklist_val.append(i.val)
        n = self.min_value_location(linklist_val)
        lists[n].next = self.mergeKLists(lists)  # 这里的lists中第n个应该为lists[n].next 用c++比较容易实现，python貌似不太适合链表操作
        return lists[n]

    def min_value_location(self, list):
        location = 0
        min = list[0]
        for i in range(len(list)):
            if list[i] < min:
                min = list[i]
                location = i
        return location
