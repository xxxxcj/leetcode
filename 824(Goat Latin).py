class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        vowel = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
                 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}

        for idx in range(len(words)):
            if words[idx][0] in vowel:
                words[idx] += 'ma' + 'a' + 'a' * idx
            else:
                words[idx] = words[idx][1:] + words[idx][0] + 'ma' + 'a' + 'a' * idx

        goat_sentence = ""
        for w in words:
            goat_sentence += w + ' '

        return goat_sentence[:-1]


sol = Solution()
sentence = "I speak Goat Latin"
print(sol.toGoatLatin(sentence))