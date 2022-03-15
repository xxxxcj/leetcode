class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        max_diff = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff > 0 and diff > max_diff:
                    max_diff = diff
        return max_diff


# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans, premin = -1, nums[0]
#
#         for i in range(1, n):
#             if nums[i] > premin:
#                 ans = max(ans, nums[i] - premin)
#             else:
#                 premin = nums[i]
#
#         return ans