class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        words_len = []
        n = len(words)

        for word in words:
            words_len.append(len(word))

        word_pos = [[words_len[0]]]
        col_pos = words_len[0] + 1

        for length in words_len[1:]:
            if col_pos + length > maxWidth:
                word_pos.append([length])
                col_pos = length + 1
            else:
                col_pos += length + 1
                word_pos[-1].append(length)

        result = []
        pos = 0
        for row in word_pos[:-1]:
            row_word_len = sum(row)
            result.append(words[pos])
            pos += 1
            if len(row) != 1:
                space_num = (maxWidth - row_word_len) // (len(row) - 1)
                remainder = (maxWidth - row_word_len) % (len(row) - 1)
                for i in range(len(row) - 1):
                    result[-1] += ' ' * (space_num + (i < remainder)) + words[pos]
                    pos += 1
            else:
                result[-1] += ' ' * (maxWidth - row[0])

        result.append(words[pos])
        pos += 1
        while pos < n:
            result[-1] += ' ' + words[pos]
            pos += 1

        result[-1] += ' ' * (maxWidth - len(result[-1]))

        return result


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
result = Solution().fullJustify(words, maxWidth)
for i in result:
    print(i)
