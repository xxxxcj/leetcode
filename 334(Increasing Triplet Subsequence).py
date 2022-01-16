class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # i, j, k = 0, 1, 2
        # if len(nums) < 3:
        #     return False
        #
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] < nums[j]:
        #             k = j + 1
        #             while k < len(nums):
        #                 if nums[j] < nums[k]:
        #                     return True
        #                 k += 1
        #         j += 1
        #     i += 1
        # return False

        n = len(nums)
        if n < 3:
            return False
        leftMin = [0] * n
        leftMin[0] = nums[0]
        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i])
        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])
        for i in range(1, n - 1):
            if leftMin[i - 1] < nums[i] < rightMax[i + 1]:
                return True
        return False

nums = []
sol = Solution()
print(sol.increasingTriplet(nums))
