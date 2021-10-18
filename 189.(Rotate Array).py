class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        tmp = nums[n-k:]
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]

        for i in range(k):
            nums[i] = tmp[i]

        print(nums)


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
sol.rotate(nums, k)
