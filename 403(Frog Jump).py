class Solution:
    def canCross(self, stones: list) -> bool:
        n = len(stones)

        dp = [[False for _ in range(n)]]

        def dfs(i, k):

            if k > len(dp) - 1:
                for _ in range(len(dp), k + 1):
                    dp.append([False for _ in range(n)])

            if dp[k][i]:
                return

            dp[k][i] = True
            j = i + 1

            while j < n and stones[j] <= stones[i] + k + 1:
                if stones[i] + k - 1 == stones[j]:
                    dfs(j, k - 1)
                elif stones[i] + k == stones[j]:
                    dfs(j, k)
                elif stones[i] + k + 1 == stones[j]:
                    dfs(j, k + 1)
                j += 1

        if stones[1] != 1:
            return False

        dfs(1, 1)

        for i in range(len(dp)):
            if dp[i][-1]:
                return True

        return False


stones = [0,1,2,3,4,8,9,11]
print(Solution().canCross(stones))
