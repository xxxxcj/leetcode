class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        num_empty = 0
        while numBottles:
            ans += numBottles
            num_empty += numBottles
            numBottles = num_empty // numExchange
            num_empty %= numExchange
            # print(num_empty, numBottles)
        return ans


numBottles = 5
numExchange = 5
sol = Solution()
print(sol.numWaterBottles(numBottles,numExchange))