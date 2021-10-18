class Solution:
    def combinationSum4(self, nums: list, target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(1, target+1):
            for j in range(len(nums)):
                if i-nums[j] > -1:
                    dp[i] += dp[i-nums[j]]

        return dp[-1]


nums = [3]
target = 9
print(Solution().combinationSum4(nums,target))