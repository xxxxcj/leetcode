class Solution:
    def permuteUnique(self, nums: list) -> list:
        ans = []

        def my_permute(li: list, nums: list):
            used_element = []
            if len(nums) == 0:
                ans.append(li)
            else:
                for i in range(len(nums)):
                    if nums[i] not in used_element:
                        used_element.append(nums[i])
                        my_permute(li + [nums[i]], nums[:i] + nums[i + 1:])

        my_permute([], nums)

        return ans


nums = [3, 3, 0, 3]
print(Solution().permuteUnique(nums))
