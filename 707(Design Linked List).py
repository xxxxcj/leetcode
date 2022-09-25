class Node:
    def __init__(self):
        self.val = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        p = self.head.next
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        p = Node()
        p.val = val
        p.next = self.head.next
        self.head = p
        self.length += 1

    def addAtTail(self, val: int) -> None:
        p = self.head.next
        while p.next is not None:
            p = p.next
        q = Node()
        q.val = val
        p.next = q
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        p = self.head
        for _ in range(index):
            p = p.next
        q = Node()
        q.val = val
        q.next = p.next
        p.next = q
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        p = self.head
        for _ in range(index):
            p = p.next
        p.next = p.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
