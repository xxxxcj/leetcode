class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:needle_len + i] == needle:
                return i
        return -1


haystack = "baaaaaaaa"
needle = "bagytisyy"

print(Solution().strStr(haystack, needle))
