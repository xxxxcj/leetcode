class Solution:
    def checkPossibility(self, nums: list) -> bool:
        def is_non_decreasing():
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True

        if len(nums) < 2:
            return True

        if nums[0] > nums[1]:
            nums[0] = nums[1]
            return is_non_decreasing()

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i+1]:
                tmp = nums[i]
                nums[i] = nums[i-1]
                if is_non_decreasing():
                    return True
                else:
                    nums[i], nums[i+1] = tmp, tmp
                    return is_non_decreasing()
        return True


nums = [4, 2, 3]
print(Solution().checkPossibility(nums))
