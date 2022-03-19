class Solution:
    def totalMoney(self, n: int) -> int:
        num_of_weeks = n // 7
        m = n % 7
        return 28 * num_of_weeks + 7 * (num_of_weeks - 1) * num_of_weeks // 2 + m * num_of_weeks + m * (m + 1) // 2


print(Solution().totalMoney(10))
