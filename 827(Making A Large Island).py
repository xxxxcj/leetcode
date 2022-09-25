class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_size = [[(0, -1) for _ in range(n)] for _ in range(n)]

        is_visited = [[False for _ in range(n)] for _ in range(n)]

        stk = []
        island_idx = 0
        for i in range(n):
            for j in range(n):
                if not is_visited[i][j]:
                    is_visited[i][j] = True
                    if grid[i][j] == 1:
                        stk.append((i, j))
                        size = 1
                        visited_island = [(i, j)]
                        while len(stk) != 0:
                            x = stk[-1][0]
                            y = stk[-1][1]
                            stk.pop()
                            if x + 1 < n and grid[x + 1][y] == 1 and not is_visited[x + 1][y]:
                                is_visited[x + 1][y] = True
                                stk.append((x + 1, y))
                                visited_island.append((x + 1, y))
                                size += 1
                            if x - 1 >= 0 and grid[x - 1][y] == 1 and not is_visited[x - 1][y]:
                                is_visited[x - 1][y] = True
                                stk.append((x - 1, y))
                                visited_island.append((x - 1, y))
                                size += 1
                            if y + 1 < n and grid[x][y + 1] == 1 and not is_visited[x][y + 1]:
                                is_visited[x][y + 1] = True
                                stk.append((x, y + 1))
                                visited_island.append((x, y + 1))
                                size += 1
                            if y - 1 >= 0 and grid[x][y - 1] == 1 and not is_visited[x][y - 1]:
                                is_visited[x][y - 1] = True
                                stk.append((x, y - 1))
                                visited_island.append((x, y - 1))
                                size += 1
                        while len(visited_island) != 0:
                            island_size[visited_island[-1][0]][visited_island[-1][1]] = (size, island_idx)
                            visited_island.pop()
                        island_idx += 1

        max_size = 0
        for i in range(n):
            for j in range(n):
                size = 0
                island_idx = []
                if grid[i][j] == 0:
                    size += 1
                    if i - 1 >= 0 and island_size[i - 1][j][1] not in island_idx:
                        size += island_size[i - 1][j][0]
                        island_idx.append(island_size[i - 1][j][1])
                    if i + 1 < n and island_size[i + 1][j][1] not in island_idx:
                        size += island_size[i + 1][j][0]
                        island_idx.append(island_size[i + 1][j][1])
                    if j - 1 >= 0 and island_size[i][j - 1][1] not in island_idx:
                        size += island_size[i][j - 1][0]
                        island_idx.append(island_size[i][j - 1][1])
                    if j + 1 < n and island_size[i][j + 1][1] not in island_idx:
                        size += island_size[i][j + 1][0]
                        island_idx.append(island_size[i][j + 1][1])
                max_size = max(size, max_size)
        if max_size == 0:
            return n*n
        return max_size


grid = [[1, 1], [1, 1]]
sol = Solution()
print(sol.largestIsland(grid))
