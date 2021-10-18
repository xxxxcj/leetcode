class Solution:
    def search(self, nums: list, target: int) -> bool:

        def binary_search(left, right):
            mid = (left + right)//2
            if target == nums[mid]:
                return True
            if left > right:
                return False
            if nums[left] <= target < nums[mid]:
                return binary_search(left, mid - 1)
            if nums[mid] < target <= nums[right]:
                return binary_search(mid + 1, right)
            return binary_search(left, mid - 1) or binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)


nums = [2,5,6,0,0,1,2]
for i in nums:
    print(Solution().search(nums, i))
