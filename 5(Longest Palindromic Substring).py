class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        centre = 0
        ans = ""
        while centre < len(s):
            i = 1
            while centre - i >= 0 and centre + i < len(s) and s[centre + i] == s[centre - i]:
                i += 1
            if 2 * i - 1 > len(ans):
                ans = s[centre - i + 1: centre + i]
                # print(ans, centre)
            i = 1
            while centre - i + 1 >= 0 and centre + i < len(s) and s[centre + i] == s[centre - i + 1]:
                i += 1
            if 2 * (i - 1) > len(ans):
                ans = s[centre - i + 2: centre + i]
                # print(ans, centre)
            centre += 1
        return ans


s = "abaaaaabaabaaaaa"
print(Solution().longestPalindrome(s))
