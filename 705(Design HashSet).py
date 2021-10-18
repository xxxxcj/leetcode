class Node:
    def __init__(self, key):
        self.val = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [Node(-1) for _ in range(10000)]

    def add(self, key: int) -> None:
        i = key % 10000
        p = self.hash[i]
        while p.next is not None:
            p = p.next
        p.next = Node(key)

    def remove(self, key: int) -> None:
        i = key % 10000
        p = self.hash[i]
        while p.next is not None:
            if p.next.val == key:
                p.next = p.next.next
                return
            p = p.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = key % 10000
        p = self.hash[i]
        while p.next is not None:
            if p.next.val == key:
                return True
            p = p.next
        return False
