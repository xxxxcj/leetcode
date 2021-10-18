class Solution:
    def exist(self, board: list, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)

        def exist(i, j, l):
            if board[i][j] != word[l]:
                return False

            if l == word_len - 1:
                return True

            result = False
            visited.append((i, j))
            if i+1 < m and (i+1, j) not in visited and exist(i+1, j, l+1):
                result = True
            elif 0 <= i-1 and (i-1, j) not in visited and exist(i-1, j, l+1):
                result = True
            elif j+1 < n and (i, j+1) not in visited and exist(i, j+1, l+1):
                result = True
            elif 0 <= j-1 and (i, j-1) not in visited and exist(i, j-1, l+1):
                result = True

            visited.remove((i,j))
            return result

        for i in range(m):
            for j in range(n):
                visited = []
                if board[i][j] == word[0] and exist(i, j, 0):
                    return True
        return False


board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"

print(Solution().exist(board, word))

