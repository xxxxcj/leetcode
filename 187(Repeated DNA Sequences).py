class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        DNA_dict = {}
        for i in range(len(s)-9):
            if s[i:i+10] not in DNA_dict:
                DNA_dict[s[i: i + 10]] = 1
            else:
                DNA_dict[s[i: i + 10]] += 1

        return [_ for _ in DNA_dict if DNA_dict[_] > 1]


sol = Solution()
s = "AAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))
