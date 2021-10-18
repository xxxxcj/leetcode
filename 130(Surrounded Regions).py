class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def change_board_flag(i, j):
            if 0 <= i < col_num and 0 <= j < row_num and board[i][j] == 'O' and not board_flag[i][j]:
                board_flag[i][j] = True
                change_board_flag(i + 1, j)
                change_board_flag(i - 1, j)
                change_board_flag(i, j + 1)
                change_board_flag(i, j - 1)

        col_num = len(board)
        if col_num == 0:
            return
        row_num = len(board[0])

        board_flag = [[False for x in range(row_num)] for x in range(col_num)]
        for i in range(col_num):
            for j in range(row_num):
                if (i == 0 or i == col_num - 1 or j == 0 or j == row_num - 1) and board[i][j] == "O" and not board_flag[i][j]:
                    change_board_flag(i, j)

        for i in range(col_num):
            for j in range(row_num):
                if board[i][j] == 'O' and not board_flag[i][j]:
                    board[i][j] = "X"

board = [["X","O","X"],
         ["O","X","O"],
         ["X","O","X"]]
Solution().solve(board)
for i in board:
    print(i)
