class Solution:
    def validTicTacToe(self, board: list) -> bool:
        Xs, Os = 0, 0

        for i in range(3):
            board[i] = list(board[i])

        for row in board:
            for ch in row:
                if ch == 'X':
                    Xs += 1
                elif ch == 'O':
                    Os += 1

        if Xs - Os > 1 or Xs < Os:
            return False

        X3 = 0
        O3 = 0
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == "X":
                X3 += 1
                board[i][0] = " "
                board[i][1] = " "
                board[i][2] = " "

            if board[i][0] == board[i][1] == board[i][2] == "O":
                O3 += 1
                board[i][0] = " "
                board[i][1] = " "
                board[i][2] = " "

            if board[0][i] == board[1][i] == board[2][i] == 'X':
                X3 += 1
                board[2][i] = ' '
                board[2][i] = ' '
                board[2][i] = ' '

            if board[0][i] == board[1][i] == board[2][i] == 'O':
                O3 += 1
                board[2][i] = ' '
                board[2][i] = ' '
                board[2][i] = ' '

        if board[0][0] == board[1][1] == board[2][2] == 'X':
            X3 += 1
            board[0][0] = ' '
            board[1][1] = ' '
            board[2][2] = ' '
        if board[0][0] == board[1][1] == board[2][2] == 'O':
            O3 += 1
            board[0][0] = ' '
            board[1][1] = ' '
            board[2][2] = ' '

        if board[0][2] == board[1][1] == board[2][0] == 'X':
            X3 += 1
            board[0][2] = ' '
            board[1][1] = ' '
            board[2][0] = ' '

        if board[0][2] == board[1][1] == board[2][0] == 'O':
            O3 += 1
            board[0][2] = ' '
            board[1][1] = ' '
            board[2][0] = ' '

        return (X3 == 0 and O3 == 0) or \
               (X3 == 1 and O3 == 0 and Xs - Os == 1) or \
               (X3 == 0 and O3 == 1 and Xs == Os)


board = ["XOX",
         "OXO",
         "XOX"]
sol = Solution()
print(sol.validTicTacToe(board))
