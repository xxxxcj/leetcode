class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n, m = len(heights), len(heights[0])

        is_reach_pacific = [[False for _ in range(m)] for _ in range(n)]
        is_reach_atlantic = [[False for _ in range(m)] for _ in range(n)]

        def visit(i: int, j:int, is_reach_map: list):
            is_reach_map[i][j] = True
            if i + 1 < n and not is_reach_map[i+1][j] and heights[i][j] <= heights[i+1][j]:
                visit(i+1, j, is_reach_map)
            if i - 1 >= 0 and not is_reach_map[i-1][j] and heights[i][j] <= heights[i-1][j]:
                visit(i-1, j, is_reach_map)
            if j + 1 < m and not is_reach_map[i][j+1] and heights[i][j] <= heights[i][j+1]:
                visit(i, j+1, is_reach_map)
            if j - 1 >= 0 and not is_reach_map[i][j-1] and heights[i][j] <= heights[i][j-1]:
                visit(i, j-1, is_reach_map)

        for j in range(m):
            visit(0, j, is_reach_pacific)
            visit(n-1, j, is_reach_atlantic)

        for i in range(n):
            visit(i, 0, is_reach_pacific)
            visit(i, m-1, is_reach_atlantic)

        ans = []
        for i in range(n):
            for j in range(m):
                if is_reach_pacific[i][j] and is_reach_atlantic[i][j]:
                    ans.append([i, j])

        return ans

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))