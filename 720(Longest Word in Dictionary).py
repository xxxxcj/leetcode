class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort(key=lambda x:len(x))

        word_dict = {}
        for w in words:
            if len(w) == 1:
                word_dict[w] = 1
            elif w[:-1] in word_dict:
                word_dict[w] = 1

        max_len = 0
        ret = []
        for key in word_dict:
            if len(key) > max_len:
                max_len = len(key)
                ret = [key]
            elif len(key) == max_len:
                ret.append(key)

        def dict_order(a: str, b:str):
            for i in range(min(len(a), len(b))):
                if ord(a[i]) < ord(b[i]):
                    return a
                elif ord(a[i]) > ord(b[i]):
                    return b

            if len(a) < len(b):
                return a
            return b

        if len(ret) == 0:
            return ""

        ans = ret[0]
        for i in range(1, len(ret)):
            ans = dict_order(ans, ret[i])

        return ans

words = ["a","banana","app","appl","ap","apply","apple"]
sol = Solution()
print(sol.longestWord(words))