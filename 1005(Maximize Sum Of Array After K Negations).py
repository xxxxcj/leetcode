class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)
        idx = 0
        while k > 0 and idx < len(nums):
            if nums[idx] < 0:
                nums[idx] = -nums[idx]
                k -= 1
            idx += 1
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2 * nums[-1]


nums = [4, 2, 3]
k = 1
sol = Solution()
print(sol.largestSumAfterKNegations(nums, k))
