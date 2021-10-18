class Solution:
    def minCost(self, houses: list, cost: list, m: int, n: int, target: int) -> int:
        # dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        #
        # for i in range(n):
        #     dp[0][i][0] = cost[0][i]
        #
        # for j in range(m-1):
        #     for i in range(n):
        #         dp[j][i][0] = dp[j-1][i]

        dp = [[[float('inf'), 0] for _ in range(target)] for _ in range(m)]

        min_v = float('inf')
        min_index = 0

        for i in range(n):
            if min_v > cost[0][i]:
                min_v = cost[0][i]
                min_index = i

        dp[0][0] = [min_v, min_index + 1]

        i = 1
        while i < m:
            dp[i][0][0] = dp[i - 1][0][0] + cost[i][dp[i - 1][0][1] - 1]
            dp[i][0][1] = dp[i - 1][0][1]

            for t in range(1, target):
                min_v = float('inf')
                min_index = 0

                for q in range(n):
                    if min_v > cost[i][q]:
                        min_v = cost[i][q]
                        min_index = q

                if min_index + 1 != dp[i - 1][t - 1][1] and min_v + dp[i - 1][t - 1][0] < dp[i - 1][t][0] + cost[i][
                    dp[i - 1][t][1] - 1]:
                    dp[i][t][0] = min_v + dp[i - 1][t - 1][0]
                    dp[i][t][1] = min_index + 1
                else:
                    dp[i][t][0] = dp[i - 1][t][0] + cost[i][dp[i - 1][t][1] - 1]
                    dp[i][t][1] = dp[i - 1][t][1]
            i += 1

        for i in dp:
            print(i)

        return dp[-1][-1][0]


houses = [0, 2, 1, 2, 0]
cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
m = 5
n = 2
target = 3

print(Solution().minCost(houses, cost, m, n, target))
