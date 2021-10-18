class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[1, 0, 1]]
        for i in range(1, n):
            dp.append([dp[-1][0] + dp[-1][1], dp[-1][0], dp[-1][0]*2 + dp[-1][1]])
        return dp[-1][2]


print(Solution().climbStairs(4))