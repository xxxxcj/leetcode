class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        frequency = [0 for _ in range(26)]

        for i in range(len(s)):
            frequency[ord(s[i]) - ord('a')] += 1

        invalid = []
        for i in range(26):
            if 0 < frequency[i] < k:
                invalid.append(i)

        if len(invalid) == 0:
            return len(s)

        j = 0
        result = []
        for i in range(len(s)):
            if ord(s[i]) - ord('a') in invalid:
                result.append(self.longestSubstring(s[j:i], k))
                j = i + 1

        result.append(self.longestSubstring(s[j:len(s)], k))

        return max(result)


s = "ababacb"
k = 3
print(Solution().longestSubstring(s, k))