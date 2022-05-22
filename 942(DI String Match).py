class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        integers = list(range(len(s) + 1))

        num_I = s.count('I')

        I_list = integers[:num_I + 1]
        D_list = integers[num_I + 1:]

        i = 0
        d = 0
        ans = []
        for ch in s:
            if ch == "I":
                ans.append(I_list[i])
                i += 1
            else:
                ans.append(D_list[-d - 1])
                d += 1
        print(i, I_list, d, D_list)
        if i != len(I_list):
            ans.append(I_list[-1])
        else:
            ans.append(D_list[0])

        return ans


s = "IDIDDDDIDIIIDIIIDDDD"
print(Solution().diStringMatch(s))
