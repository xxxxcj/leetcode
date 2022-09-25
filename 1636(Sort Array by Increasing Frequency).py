class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        freq_num = []
        for num in num_dict:
            freq_num.append((num, num_dict[num]))

        freq_num.sort(key=lambda x: (x[1], -x[0]))

        res = []

        for x in freq_num:
            for y in range(x[1]):
                res.append(x[0])

        return res


nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
sol = Solution()
print(sol.frequencySort(nums))
