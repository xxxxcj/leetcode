class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        ans = 0
        s_len = len(s)
        s_dict = {}
        while right < s_len:
            if s[right] not in s_dict:
                s_dict[s[right]] = right
                right += 1
            else:
                ans = max(ans, right - left)
                s_dict.pop(s[left])
                left += 1
        ans = max(ans, right - left)
        return ans


string = "aaaaaaadaaaaaaaa"
print(Solution().lengthOfLongestSubstring(string))
