class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        rows = len(board)
        cols = len(board[0])

        def find_a_word(word: str, i: int, visited: list):
            if i == 0:
                flag = False
                for r in range(rows):
                    for c in range(cols):
                        if board[r][c] == word[i]:
                            visited_new = visited.copy()
                            visited_new.append((r, c))
                            flag = flag or find_a_word(word, 1, visited_new)
                return flag
            elif i < len(word):
                r = visited[-1][0]
                c = visited[-1][1]
                flag = False
                if r + 1 < rows and (r + 1, c) not in visited and word[i] == board[r + 1][c]:
                    visited_new = visited.copy()
                    visited_new.append((r + 1, c))
                    flag = flag or find_a_word(word, i + 1, visited_new)
                if c + 1 < cols and (r, c + 1) not in visited and word[i] == board[r][c + 1]:
                    visited_new = visited.copy()
                    visited_new.append((r, c + 1))
                    flag = flag or find_a_word(word, i + 1, visited_new)
                if r - 1 >= 0 and (r - 1, c) not in visited and word[i] == board[r - 1][c]:
                    visited_new = visited.copy()
                    visited_new.append((r - 1, c))
                    flag = flag or find_a_word(word, i + 1, visited_new)
                if c - 1 >= 0 and (r, c - 1) not in visited and word[i] == board[r][c - 1]:
                    visited_new = visited.copy()
                    visited_new.append((r, c - 1))
                    flag = flag or find_a_word(word, i + 1, visited_new)

                return flag

            elif i == len(word):
                return True

        # print(find_a_word(words[0], 0, []))
        ans = []
        for word in words:
            if find_a_word(word, 0, []):
                ans.append(word)
        return ans


board = [["a", "b", "c"],
         ["a", "e", "d"],
         ["a", "f", "g"]]
words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]

sol = Solution()
print(sol.findWords(board, words))
