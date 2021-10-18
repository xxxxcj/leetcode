class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        # python中的list是已经做了hash处理的
        i = 1
        while i in nums:
            i += 1
        return i


nums = [1, 2, 0]
print(Solution().firstMissingPositive(nums))
