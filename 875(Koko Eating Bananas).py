import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def eating_time(k: int):
            t = 0
            for b in piles:
                t += math.ceil(b/k)
            return t

        left, right = 0, max(piles)
        while left < right:
            mid = (left + right) // 2
            if mid == 0:
                return 1
            t = eating_time(mid)
            if t > h:
                left = mid + 1
            else:
                right = mid
        return left


piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h = 823855818
print(Solution().minEatingSpeed(piles, h))
