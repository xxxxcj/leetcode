class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = list()
        words_len = len(words)
        for i in range(words_len):
            mask = 0
            for ch in words[i]:
                mask |= 1 << ord(ch) - ord('a')
            masks.append(mask)

        maxP = 0
        for i in range(words_len):
            for j in range(i+1, words_len):
                if not masks[i] & masks[j]:
                    maxP = max(len(words[i])*len(words[j]), maxP)

        return maxP
