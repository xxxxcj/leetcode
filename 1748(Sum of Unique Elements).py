class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        num_dict = {}

        ans = 0
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
                ans += num
            else:
                if num_dict[num] == 1:
                    ans -= num
                num_dict[num] += 1

        return ans
