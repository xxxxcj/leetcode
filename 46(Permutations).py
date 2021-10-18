class Solution:
    def permute(self, nums: list) -> list:
        ans = []

        def my_permute(li: list, nums: list):
            if len(nums) == 0:
                ans.append(li)
            else:
                for i in range(len(nums)):
                    my_permute(li + [nums[i]], nums[:i]+nums[i + 1:])

        my_permute([], nums)

        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
