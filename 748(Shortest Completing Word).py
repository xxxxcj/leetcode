class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list) -> str:
        lP_dict = {}
        for ch in licensePlate:
            if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
                if ch.lower() not in lP_dict:
                    lP_dict[ch.lower()] = 1
                else:
                    lP_dict[ch.lower()] += 1

        ans = ""
        for word in words:
            word_dict = {}
            for ch in word:
                if ch in word_dict:
                    word_dict[ch] += 1
                else:
                    word_dict[ch] = 1

            flag = True
            for key in lP_dict:
                if key not in word_dict:
                    flag = False
                    break
                elif word_dict[key] < lP_dict[key]:
                    flag = False
                    break

            if flag:
                if len(ans) > len(word) or ans == "":
                    ans = word

        return ans


licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
sol = Solution()
print(sol.shortestCompletingWord(licensePlate, words))