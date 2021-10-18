class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        max_average = sum(nums[0:k])
        last_average = max_average
        for i in range(len(nums) - k):
            a, b = nums[i], nums[k + i]
            last_average = last_average - a + b
            if last_average > max_average:
                max_average = last_average
        return max_average / k
