class Solution:
    def commonChars(self, A: list) -> list:
        min_frequency = [float('inf')] * 26
        for s in A:
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - ord("a")] += 1
            for i in range(26):
                min_frequency[i] = min(min_frequency[i], frequency[i])

        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * min_frequency[i])

        return ans
