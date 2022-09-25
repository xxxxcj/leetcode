class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        min_pos_dict = {}
        max_len = -1
        for idx, ch in enumerate(s):
            if ch not in min_pos_dict:
                min_pos_dict[ch] = idx
            else:
                max_len = max(max_len, idx - min_pos_dict[ch] - 1)
        return max_len