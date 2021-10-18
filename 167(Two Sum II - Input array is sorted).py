class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        num_dict = {}
        for idx, item in enumerate(numbers):
            num_dict[item] = idx

        for idx, num in enumerate(numbers):
            if target - num in num_dict and idx != num_dict[target-num]:
                return [idx+1, num_dict[target-num]+1]