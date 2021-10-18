class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:

        def put(num):
            if num != nums[num - 1]:
                tmp = nums[num - 1]
                nums[num - 1] = num
                put(tmp)

        for i in nums:
            put(i)

        result = []
        for idx, item in enumerate(nums):
            if item-1 != idx:
                result.append(idx+1)
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))
