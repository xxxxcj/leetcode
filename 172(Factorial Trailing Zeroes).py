class Solution:
    def trailingZeroes(self, n: int) -> int:
        # num_zero = 0
        # num = 1
        # result = 1
        # while num <= n:
        #     result *= num
        #     num += 1
        #     while result % 10 == 0:
        #         num_zero += 1
        #         result //= 10
        #
        # return num_zero

        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans


sol = Solution()
print(sol.trailingZeroes(9070))