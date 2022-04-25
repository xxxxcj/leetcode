class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        max_f = 0

        sum_of_nums = 0
        for idx, item in enumerate(nums):
            max_f += idx * item
            sum_of_nums += item

        f = max_f

        for i in range(1, len(nums)):
            f -= sum_of_nums
            f += len(nums) * nums[i-1]

            if f > max_f:
                max_f = f

        return max_f

