class Solution:
    def findCircleNum(self, M: list) -> int:
        # 不相交集
        # friend_cycles = [[x] for x in range(len(M))]
        # for i in range(len(M)):
        #     for j in range(i + 1, len(M[0])):
        #         if M[i][j] == 1:
        #             for a_cycle in friend_cycles:
        #                 if i in a_cycle:
        #                     for b_cycle in friend_cycles:
        #                         if j in b_cycle:
        #                             if a_cycle != b_cycle:
        #                                 a_cycle.extend(b_cycle)
        #                                 friend_cycles.remove(b_cycle)
        #                                 break
        #                     break
        # return len(friend_cycles)

        # dfs
        visited = [False for x in range(len(M))]
        count = 0

        def dfs(n):
            if not visited[n]:
                visited[n] = True
                for i in range(len(M[n])):
                    if M[n][i] == 1:
                        dfs(i)

        for i in range(len(M)):
            if not visited[i]:
                dfs(i)
                count += 1

        return count



M = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(M))

