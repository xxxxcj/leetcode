class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        sum_range = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    w_min, w_max = nums[j], nums[j]
                else:
                    if nums[j] > w_max:
                        w_max = nums[j]
                    elif nums[j] < w_min:
                        w_min = nums[j]
                    sum_range += w_max - w_min
        return sum_range
