from queue import Queue

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        english_letters_stk = []
        other_characters = Queue()
        other_characters_pos = []

        for idx, ch in enumerate(s):
            if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
                english_letters_stk.append(ch)
            else:
                other_characters.put(ch)
                other_characters_pos.append(idx)

        j = 0
        ans = ''
        for i in range(len(s)):
            if j < len(other_characters_pos) and i == other_characters_pos[j]:
                j += 1
                ans += other_characters.get()
            else:
                ans += english_letters_stk.pop()

        return ans