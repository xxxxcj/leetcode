from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
booking = [[47, 50], [1, 10], [27, 36], [40, 47], [20, 27], [15, 23], [10, 18], [27, 36], [17, 25], [8, 17], [24, 33],
           [23, 28], [21, 27], [47, 50], [14, 21], [26, 32], [16, 21], [2, 7], [24, 33], [6, 13], [44, 50], [33, 39],
           [30, 36], [6, 15], [21, 27], [49, 50], [38, 45], [4, 12], [46, 50], [13, 21]]
obj = MyCalendarThree()
for b in booking:
    print(obj.book(b[0], b[1]), end=" ")
