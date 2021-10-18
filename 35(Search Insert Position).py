class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
            mid = (left + right) // 2
        return mid + 1


nums = []
target = 1
print(Solution().searchInsert(nums, target))
