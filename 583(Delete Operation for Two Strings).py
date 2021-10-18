class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        if word1[0] == word2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 2

        for i in range(1, n):
            if word1[0] != word2[i]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = i

        for i in range(1, m):
            if word2[0] != word1[i]:
                dp[0][i] = dp[0][i-1] + 1
            else:
                dp[0][i] = i

        for i in range(1, n):
            for j in range(1, m):
                if word1[j] != word2[i]:
                    dp[i][j] = min(dp[i][j - 1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j - 1] + 1, dp[i-1][j] + 1)

        for i in dp:
            print(i)

        return dp[n - 1][m - 1]


sol = Solution()
word1 = "leetcode"
word2 = "etco"
print(sol.minDistance(word1, word2))
