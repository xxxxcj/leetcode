class Solution:
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        if nums[-1] > 0:
            if nums[0] * nums[1] > nums[-2] * nums[-3]:
                return nums[0] * nums[1]*nums[-1]
            else:
                return nums[-2] * nums[-3]*nums[-1]
        else:
            if nums[0] * nums[1] < nums[-2] * nums[-3]:
                return nums[0] * nums[1]*nums[-1]
            else:
                return nums[-2] * nums[-3]*nums[-1]


nums = [-1, -2, -3, 4]
sol = Solution()
print(sol.maximumProduct(nums))
