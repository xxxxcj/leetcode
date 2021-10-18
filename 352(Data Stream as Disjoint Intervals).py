class SummaryRanges:

    def __init__(self):
        self.nums = [0 for _ in range(10 ** 4 + 1)]

    def addNum(self, val: int) -> None:
        self.nums[val] += 1

    def getIntervals(self) -> list[list[int]]:
        intervals = list()
        start, end = -1, -1
        for i in range(10 ** 4 + 1):
            if self.nums[i] != 0:
                if start == -1:
                    start = i
                    end = i
                else:
                    end += 1
            else:
                if start != -1:
                    intervals.append([start, end])
                    start, end = -1, -1
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
