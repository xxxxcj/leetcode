class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        s1_dict, s2_dict = [0]*26, [0]*26

        for i in s1:
            s1_dict[ord(i) - ord('a')] += 1

        for i in s2[:s1_len]:
            s2_dict[ord(i) - ord('a')] += 1

        if s1_dict == s2_dict:
            return True

        for i in range(s1_len, s2_len):
            s2_dict[ord(s2[i]) - ord('a')] += 1
            s2_dict[ord(s2[i-s1_len]) - ord('a')] -= 1
            if s1_dict == s2_dict:
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))