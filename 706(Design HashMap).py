class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [Node(-1, -1) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % 1000
        p = self.map[i]
        while p.next is not None:
            if p.next.key == key:
                p.next.val = value
                return
            p = p.next
        p.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % 1000
        p = self.map[i]
        while p.next is not None:
            if p.next.key == key:
                return p.next.val
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % 1000
        p = self.map[i]
        while p.next is not None:
            if p.next.key == key:
                p.next = p.next.next
                return
            p = p.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
