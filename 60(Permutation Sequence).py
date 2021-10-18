class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        int_list = [str(_ + 1) for _ in range(n)]
        result = ""
        k -= 1
        while len(int_list) != 0:
            gap = self.factorial(n - 1)
            result += int_list[k // gap]
            int_list.remove(result[-1])
            k %= gap
            n -= 1
        return result

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        return n*self.factorial(n-1)


n = 4
k = 4
sol = Solution()
print(sol.getPermutation(n, k))
