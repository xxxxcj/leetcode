class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return i + 1


nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
print(nums)
