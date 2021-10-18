import re

class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        def get_dict(dict, words):
            for i in words:
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] += 1

        def match(s, dict):
            s_dict = {}
            s = re.findall(r'.{%s}' % word_len, s)
            get_dict(s_dict, s)
            if s_dict != dict:
                return False
            return True

        if len(s) == 0 or len(words) == 0:
            return []
        words_dict = {}
        get_dict(words_dict, words)
        word_len = len(words[0])
        words_list_len = len(words)
        ans = []
        for i in range(len(s)-words_list_len*word_len+1):
            if match(s[i: i + words_list_len*word_len], words_dict):
                ans.append(i)
        return ans


s = ""
words = []
print(Solution().findSubstring(s, words))

