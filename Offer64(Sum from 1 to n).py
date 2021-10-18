class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))

    # 这方法太秀了
    # def sumNums(self, n: int) -> int:
    #     return sum(range(n+1))


n = 2
print(Solution().sumNums(n))
