class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        ans = 0
        nums_dict = {}
        max_freq = 0
        max_freq_item_num = 0
        second_freq_item_num = 0
        freq_1 = {}
        for idx, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = 1
                freq_1[num] = 1
            elif nums_dict[num] == 1:
                nums_dict[num] += 1
                freq_1.pop(num)
            else:
                nums_dict[num] += 1

            if nums_dict[num] > max_freq:
                max_freq = nums_dict[num]
                second_freq_item_num = max_freq_item_num - 1
                max_freq_item_num = 1
            elif nums_dict[num] == max_freq:
                max_freq_item_num += 1
            elif nums_dict[num] == max_freq - 1:
                second_freq_item_num += 1

            if len(freq_1) == 1 and max_freq_item_num + 1 == len(nums_dict):
                ans = idx + 1
            elif max_freq_item_num == 1 and second_freq_item_num + 1 == len(nums_dict):
                ans = idx + 1
            elif len(freq_1) == len(nums_dict):
                ans = idx + 1

        return ans


nums = [1,2]
print(Solution().maxEqualFreq(nums))
