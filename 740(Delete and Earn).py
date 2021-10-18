class Solution:
    def deleteAndEarn(self, nums: list) -> int:
        maxVal = max(nums)
        total = [0 for _ in range(maxVal + 1)]

        for num in nums:
            total[num] += num

        print(total)

        dp = [0 for _ in range(len(total))]

        dp[0] = total[0]
        dp[1] = max(total[0], total[1])

        for i in range(2, len(total)):
            dp[i] = max(dp[i-2] + total[i], dp[i-1])

        return dp[-1]


nums = [3,4,2]
print(Solution().deleteAndEarn(nums))