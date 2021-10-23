class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        num_counter = dict()

        for num in nums:
            if num not in num_counter:
                num_counter[num] = 1
            else:
                num_counter[num] += 1

        th = len(nums)/3

        ans = []
        for key in num_counter:
            if num_counter[key] > th:
               ans.append(key)

        return ans