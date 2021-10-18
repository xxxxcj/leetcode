class Solution:
    def merge(self, intervals: list):
        if len(intervals) == 0:
            return []
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[- 1][1]:
                if ans[-1][1] < intervals[i][1]:
                    ans[-1] = [ans[-1][0], intervals[i][1]]
            else:
                ans.append(intervals[i])
        return ans


intervals = [[1, 4],[2, 3]]
print(Solution().merge(intervals))
