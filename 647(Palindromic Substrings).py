class Solution:
    def countSubstrings(self, s: str) -> int:

        def is_palindromic(s: str):
            s_len = len(s)
            mid = s_len // 2
            if s_len % 2 == 0:
                return hash(s[:mid]) == hash(s[mid:])
            else:
                return hash(s[:mid]) == hash(s[mid + 1:])

        s_len = len(s)
        count = 0

        for i in range(s_len):
            for j in range(i + 1, s_len + 1):
                if is_palindromic(s[i: j]):
                    print(s[i: j])
                    count += 1

        return count


s = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
print(Solution().countSubstrings(s))
