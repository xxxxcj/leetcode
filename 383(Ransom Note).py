class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        magazine_dict = {}

        for ch in ransomNote:
            if ch not in ransom_dict:
                ransom_dict[ch] = 1
            else:
                ransom_dict[ch] += 1

        for ch in magazine:
            if ch not in magazine_dict:
                magazine_dict[ch] = 1
            else:
                magazine_dict[ch] += 1

        for key in ransom_dict:
            if key not in magazine_dict or ransom_dict[key] > magazine_dict[key]:
                return False
        return True