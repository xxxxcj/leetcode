class Solution:
    def findMin(self, nums: list) -> int:

        def binary_search(left, right):
            mid = (left + right) // 2
            if left == right:
                return nums[mid]
            elif right - left == 1:
                return min(nums[left], nums[right])
            if nums[left] > nums[mid]:
                return binary_search(left, mid)
            elif nums[mid] > nums[right]:
                return binary_search(mid, right)
            return nums[left]

        return binary_search(0, len(nums) - 1)


nums = [3,0,1,2]
print(Solution().findMin(nums))