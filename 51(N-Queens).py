class Solution:
    def solveNQueens(self, n: int) -> list:
        sol = []

        def is_valid(x, queen_pos):
            for idx, i in enumerate(queen_pos):
                if x == i or x == i - (len(queen_pos) - idx) or x == i + (len(queen_pos) - idx):
                    return False
            return True

        def find_sol(i, queen_pos):
            if i == 0:
                for j in range(n):
                    find_sol(1, [j])
            elif i == n:
                new_pos = []
                for i in queen_pos:
                    s = "."*n
                    s = s[:i] + "Q" + s[i+1:]
                    new_pos.append(s)
                sol.append(new_pos)
            else:
                for j in range(n):
                    if is_valid(j, queen_pos):
                        new_queen_pos = queen_pos.copy()
                        new_queen_pos.append(j)
                        find_sol(i+1, new_queen_pos)

        find_sol(0, [])

        return sol


sol = Solution()
print(sol.solveNQueens(10))
