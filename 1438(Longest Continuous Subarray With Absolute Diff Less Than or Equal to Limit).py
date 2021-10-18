class Solution:
    def longestSubarray(self, nums: list, limit: int) -> int:
        i = 0
        max_v, min_v = -float('inf'), float('inf')
        for j in range(len(nums)):
            if nums[j] > max_v:
                max_v = nums[j]
            if nums[j] < min_v:
                min_v = nums[j]
            if max_v - min_v > limit:
                i += 1
                if nums[i-1] == max_v:
                    max_v = max(nums[i:j+1])
                if nums[i-1] == min_v:
                    min_v = min(nums[i:j+1])

        return len(nums) - i


nums = [10,1,2,4,7,2]
limit = 5
print(Solution().longestSubarray(nums, limit))
