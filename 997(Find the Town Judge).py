class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_other_num = [0 for _ in range(n)]
        trusted_num = [0 for _ in range(n)]

        for t in trust:
            trust_other_num[t[0]-1] += 1
            trusted_num[t[1]-1] += 1

        count = 0
        label = -1
        for i in range(n):
            if trusted_num[i] == n-1 and trust_other_num[i] == 0:
                count += 1
                label = i + 1

        if count == 1:
            return label
        else:
            return -1