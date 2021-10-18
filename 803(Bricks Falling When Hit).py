class Solution:
    def hitBricks(self, grid: list, hits: list) -> list:
        width = len(grid[0])
        height = len(grid)

        def count_bricks(pos):
            result = 1
            grid[pos[0]][pos[1]] = 0
            if pos[0] == 0:
                is_fall = False
                return result, is_fall
            else:
                is_fall = True
            if pos[1] + 1 < width and grid[pos[0]][pos[1] + 1]:
                tmp = count_bricks([pos[0], pos[1] + 1])
                if tmp[1]:
                    result += 1
                else:
                    grid[pos[0]][pos[1] + 1] = 1
                    is_fall = False
            if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1]:
                tmp = count_bricks([pos[0], pos[1] - 1])
                if tmp[1]:
                    result += 1
                else:
                    grid[pos[0]][pos[1] - 1] = 1
                    is_fall = False
            if pos[0] + 1 < height and grid[pos[0] + 1][pos[1]]:
                tmp = count_bricks([pos[0] + 1, pos[1]])
                if tmp[1]:
                    result += 1
                else:
                    grid[pos[0]+1][pos[1]] = 1
                    is_fall = False
            if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]]:
                tmp = count_bricks([pos[0] - 1, pos[1]])
                if tmp[1]:
                    result += 1
                else:
                    grid[pos[0]-1][pos[1]] = 1
                    is_fall = False
            return result, is_fall

        result = []
        for pos in hits:
            result.append(count_bricks(pos)[0]-1)
            print(grid)
        return result


grids = [[1, 0, 0, 0],
         [1, 1, 1, 0]]
hits = [[1, 0]]
sol = Solution()
print(sol.hitBricks(grids, hits))
