class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph_lower = paragraph.lower().split(' ')
        words_count = {}
        banned_dict = {}

        for w in banned:
            banned_dict[w] = 1

        for tmp in paragraph_lower:
            w = ''
            for ch in tmp:
                if ord('a') <= ord(ch) <= ord('z'):
                    w += ch
                else:
                    if w not in banned_dict:
                        if w not in words_count:
                            words_count[w] = 1
                        else:
                            words_count[w] += 1
                    w = ''
            if w != '' and w not in banned_dict:
                if w not in words_count:
                    words_count[w] = 1
                else:
                    words_count[w] += 1

        max_val = 0
        max_word = ""
        for w in words_count:
            if words_count[w] > max_val:
                max_val = words_count[w]
                max_word = w

        return max_word


paragraph = "Bob"
banned = []
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
