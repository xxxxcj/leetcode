import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        n = len(envelopes)

        if n == 0:
            return 0

        envelopes.sort(key=lambda item: (item[0], -item[-1]))
        print(envelopes)
        f = [envelopes[0][1]]  # f[i]表示h的前i个元素可以组成的长度为j的最长严格递增子序列的末尾元素的最小值

        for i in range(1, n):
            num = envelopes[i][1]
            if num > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
