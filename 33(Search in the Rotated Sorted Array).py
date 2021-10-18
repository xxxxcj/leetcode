class Solution:
    def search(self, nums: list, target: int) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        if nums_len == 1:
            return 0 if target == nums[0] else -1
        left = 0
        right = nums_len - 1
        while right >= left:
            mid = (left + right) // 2
            # print(left, mid, right)
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


nums = [1,3]
target = 2
print(Solution().search(nums,target))
