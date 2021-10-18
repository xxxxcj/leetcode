class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        ptr1, ptr2 = 0, 1
        max_len = 0
        if len(nums) == 0:
            return 0
        while ptr2 < len(nums):
            if nums[ptr2] <= nums[ptr2-1]:
                if ptr2 - ptr1 > max_len:
                    max_len = ptr2 - ptr1
                ptr1 = ptr2
            ptr2 += 1

        if ptr2 - ptr1 > max_len:
            max_len = ptr2 - ptr1
        return max_len


nums = [1, 3, 5, 4, 2, 3, 4, 5]
print(Solution().findLengthOfLCIS(nums))
