class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []

        p_dict = {}
        for ch in p:
            if ch in p_dict:
                p_dict[ch] += 1
            else:
                p_dict[ch] = 1

        ans = []

        s_dict = {}
        for i in range(p_len):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

        for i in range(s_len - p_len):
            if s_dict == p_dict:
                ans.append(i)

            if s[p_len+i] in s_dict:
                s_dict[s[p_len + i]] += 1
            else:
                s_dict[s[p_len + i]] = 1

            if s_dict[s[i]] == 1:
                s_dict.pop(s[i])
            else:
                s_dict[s[i]] -= 1

        if s_dict == p_dict:
            ans.append(s_len - p_len)

        return ans