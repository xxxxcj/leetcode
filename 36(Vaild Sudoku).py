class Solution:
    def isValidSudoku(self, board: list) -> bool:
        row_list = [[] for x in range(9)]
        col_list = [[] for x in range(9)]
        box_list = [[] for x in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row = i
                    col = j
                    box = (i // 3 ) * 3 + j // 3
                    if board[i][j] in row_list[row] or board[i][j] in col_list[col] or board[i][j] in box_list[box]:
                        return False
                    else:
                        row_list[row].append(board[i][j])
                        col_list[col].append(board[i][j])
                        box_list[box].append(board[i][j])
        return True


board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(board))
