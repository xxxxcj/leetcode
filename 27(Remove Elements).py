class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i, j = 0, 0
        while i + j < len(nums):
            if nums[i + j] == val:
                j += 1
            else:
                nums[i] = nums[i + j]
                i += 1
        return i


nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums, 2))
print(nums)
