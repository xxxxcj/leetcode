class Solution:
    def matrixReshape(self, nums: list, r: int, c: int) -> list:
        n, m = len(nums), len(nums[0])
        if r * c != n * m:
            return nums

        i, j = 0, 0
        result = [[0 for _ in range(c)] for _ in range(r)]
        for two_dim_nums in nums:
            for num in two_dim_nums:
                result[j][i % c] = num
                i += 1
                j = i // c

        return result


nums = [[1, 2, 3, 4]]
r = 2
c = 2
print(Solution().matrixReshape(nums, r, c))
