class Solution:
    def singleNumber(self, nums: list) -> int:
        count_dict = dict()

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        for key in count_dict.keys():
            if count_dict[key] == 1:
                return key