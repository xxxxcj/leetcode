class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i, j = 1, 1

        num = nums[0]
        count = 1
        result = 1
        while j < len(nums):
            nums[i] = nums[j]
            if nums[j] == num:
                count += 1
                j += 1
                if count < 3:
                    i += 1
                    result += 1
            else:
                count = 1
                num = nums[j]
                i += 1
                j += 1
                result += 1

        for t in range(len(nums), i, -1):
            nums.pop()

        return result


nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))
print(nums)