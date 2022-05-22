class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # ans = 0
        # for i in range(len(nums)):
        #     tmp = nums[i]
        #     if tmp < k:
        #         ans += 1
        #         for j in range(i + 1, len(nums)):
        #             tmp *= nums[j]
        #             if tmp < k:
        #                 ans += 1
        #             else:
        #                 break
        # return ans

        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans


nums = [10, 5, 2, 6]
k = 100
sol = Solution()
print(sol.numSubarrayProductLessThanK(nums, k))
