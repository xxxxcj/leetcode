class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = 0
        for i in range(n):
            if nums[i] != 0:
                nums[p1] = nums[i]
                p1 += 1

        for i in range(p1, n):
            nums[i] = 0

sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)
