class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[0, nums[0]] for _ in range(n)]
        dp[1] = [nums[1], nums[0]]

        for i in range(2, n):
            dp[i][0] = max(dp[i-2][0] + nums[i], dp[i-1][0])
            dp[i][1] = max(dp[i-2][1] + nums[i], dp[i-1][1])

        return max(dp[-1][0], dp[-2][1])


nums = [2,1,1,2]
print(Solution().rob(nums))
