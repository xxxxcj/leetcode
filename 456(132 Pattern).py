class Solution:
    def find132pattern(self, nums: list) -> bool:
        n = len(nums)
        min_max = list()

        min, max = nums[0], nums[0]
        for i in range(1, n):
            for m in min_max:
                if m[0] < nums[i] < m[1]:
                    return True
            if min < nums[i] < max:
                return True
            if nums[i] > max:
                max = nums[i]
            elif nums[i] < min:
                min_max.append((min, max))
                min = max = nums[i]
        return False


nums = [1,3,2,4]
print(Solution().find132pattern(nums))