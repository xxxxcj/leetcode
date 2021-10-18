class Solution:
    def combine(self, n: int, k: int) -> list:
        ans = []

        def combination(start: int, k: int, nums:list):
            if k == 0:
                ans.append(nums)
            else:
                for i in range(start, n + 1):
                    combination(i + 1, k - 1, nums + [i])

        combination(1, k, [])
        return ans


n = 1
k = 1
print(Solution().combine(n, k))
