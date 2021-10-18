import numpy


class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n-1
        while j > 0:
            if nums[j - 1] < nums[j]:
                i = j
                m = nums[i]
                i_location = i
                while i < n:
                    if nums[j - 1] < nums[i] <= m:
                        m = nums[i]
                        i_location = i
                    i += 1
                tmp = nums[j - 1]
                nums[j - 1] = m
                nums[i_location] = tmp
                k, l = j, n - 1
                while k < l:
                    tmp = nums[k]
                    nums[k] = nums[l]
                    nums[l] = tmp
                    k += 1
                    l -= 1
                return
            j -= 1
        nums.sort()




nums = [2, 3, 1, 3, 3]
Solution().nextPermutation(nums)
print(nums)
