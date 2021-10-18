class Solution:
    def maxSubArray(self, nums: list) -> int:
        maxAns = nums[0]
        pre = 0
        for i in nums:
            pre = max(pre + i, i)
            maxAns = max(maxAns, pre)
        return maxAns


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
