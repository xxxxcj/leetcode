import collections


class Solution:
    def findNumOfValidWords(self, words: list, puzzles: list) -> list:
        frequency = collections.Counter()

        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))
            frequency[mask] += 1

        ans = list()

        for puzzle in puzzles:
            total = 0
            mask = 0
            for ch in puzzle:
                mask |= (1 << (ord(ch) - ord('a')))

            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask

            if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord("a"))]

            ans.append(total)

        return ans