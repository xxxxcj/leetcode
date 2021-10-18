# 该heap为min_heap，即根节点为最小值
class PriorityQueueBase:
    # 抽象基类为堆

    class Item:
        # 轻量级组合来存储堆项目
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):  # 比较大小
            return self._value < other._value

        def is_empty(self):
            return len(self) == 0

        def __str__(self):
            return str(self._key)


class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):  # 在后面加上然后加上
        self._data.append(self.Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):  # 往上交换
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):  # 往下交换，递归比较三个值
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def top(self):
        return self._data[0] if len(self._data) != 0 else -1

    def keys(self):
        keys = []
        for i in self._data:
            keys.append(i._key)
        return keys


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        frequency = hash_map.items()

        # print(frequency)

        heap = HeapPriorityQueue()
        for i in frequency:
            # print(heap.keys(), i)
            if heap.__len__() < k:
                heap.add(i[0], i[1])
            else:
                if i[1] > heap.top()._value:
                    heap.remove_min()
                    heap.add(i[0],i[1])

        return heap.keys()


k = 2
nums = [4,1,-1,2,-1,2,3]
print(Solution().topKFrequent(nums, k))

