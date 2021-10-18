class Solution:
    def pivotIndex(self, nums: list) -> int:
        nums_sum = sum(nums)
        left_sum = 0
        for idx, item in enumerate(nums):
            if nums_sum - left_sum - item == left_sum:
                return idx
            left_sum += item
        return -1
