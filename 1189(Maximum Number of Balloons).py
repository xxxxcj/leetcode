class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_dict = {'b':0, 'a':0, 'l':0, 'n':0, 'o':0}

        for ch in text:
            if ch in letter_dict:
                letter_dict[ch] += 1

        ans = len(text)
        for key, item in letter_dict.items():
            if key == 'b' or key == 'a' or key == 'n':
                ans = min(item, ans)
            else:
                ans = min(item // 2, ans)

        return ans