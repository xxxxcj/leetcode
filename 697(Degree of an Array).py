class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1

        max_element, max_times = [], 0
        for key in nums_dict:
            if max_times < nums_dict[key]:
                max_times = nums_dict[key]
                max_element = [key]
            elif max_times == nums_dict[key]:
                max_element.append(key)

        if max_times == 1:
            return 1

        i = 0
        min_len = len(nums)
        while len(max_element) != 0:
            if nums[i] not in max_element:
                i += 1
            else:
                j = len(nums) - 1
                while nums[j] != nums[i]:
                    j -= 1
                if min_len > j - i + 1:
                    min_len = j - i + 1
                max_element.remove(nums[i])

        return min_len


nums = [1,2,2,1,2,1,1,1,1,2,2,2]
print(Solution().findShortestSubArray(nums))