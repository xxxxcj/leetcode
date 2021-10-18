class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        if n == 0 or m == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = int(s[0] == t[0])

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + (s[i] == t[0])

        for j in range(1, m):
            for i in range(j, n):
                if s[i] == t[j]:
                    dp[j][i] = dp[j-1][i-1] + dp[j][i-1]
                else:
                    dp[j][i] = dp[j][i-1]

        return dp[-1][-1]


s = "babgbag"
t = "bag"
print(Solution().numDistinct(s, t))