class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        ans = []

        def combination(k, n, nums, m):
            if k == 0 and n == 0:
                ans.append(nums)
            elif (k == 0 and n != 0) or (k != 0 and n <= 0):
                return
            else:
                for i in range(m + 1, 10):
                    combination(k-1, n - i, nums + [i], i)

        combination(k, n, [], 0)

        return ans


k = 3
n = 9
print(Solution().combinationSum3(k, n))
