from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[None for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]

        def dfs(i: int, j: int, length: int):
            if dp[i][j][length] is not None:
                return dp[i][j][length]
            if s1[i: i + length] == s2[j:j + length]:
                dp[i][j][length] = True
                return True

            if Counter(s1[i: i + length]) != Counter(s2[j:j + length]):
                dp[i][j][length] = False
                return False

            for k in range(1, length):
                dp[i][j][k] = dfs(i, j, k)
                dp[i + k][j + k][length - k] = dfs(i + k, j + k, length - k)
                if dp[i][j][k] and dp[i + k][j + k][length - k]:
                    return True
                dp[i][j + length - k][k] = dfs(i, j + length - k, k)
                dp[i + k][j][length - k] = dfs(i + k, j, length - k)
                if dp[i][j + length - k][k] and dp[i + k][j][length - k]:
                    return True

            return False

        return dfs(0, 0, n)


s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
print(Solution().isScramble(s1, s2))
