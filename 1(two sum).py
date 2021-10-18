class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement], i]
            hash[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums,target))
