# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         count = [0]
#
#         def dfs(i: int):
#             if i >= n:
#                 count[0] += 1
#                 return
#             if 0 < int(s[i]):
#                 dfs(i+1)
#             if i < n-1 and 10 <= int(s[i:i+2]) < 27:
#                 dfs(i+2)
#
#         dfs(0)
#
#         return count[0]

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


s = "11111111111"
print(Solution().numDecodings(s))