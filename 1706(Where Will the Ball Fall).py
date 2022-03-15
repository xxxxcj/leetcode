class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        ans = [i for i in range(len(grid[0]))]

        for row in grid:
            for idx, pos in enumerate(ans):
                if pos != -1:
                    if pos == 0 and row[pos] == -1:
                        ans[idx] = -1
                    elif pos == len(grid[0]) - 1 and row[pos] == 1:
                        ans[idx] = -1
                    elif row[pos] != row[pos + row[pos]]:
                        ans[idx] = -1
                    else:
                        ans[idx] += row[pos]

        return ans


grid =[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
sol = Solution()
print(sol.findBall(grid))
