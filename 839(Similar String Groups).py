class Solution:
    def numSimilarGroups(self, strs: list) -> int:
        n = len(strs)
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def is_similar(x, y):
            different_char = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    different_char += 1
                if different_char > 2:
                    return False
            return True

        for i in range(n-1):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if is_similar(strs[i], strs[j]):
                    f[fi] = fj

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret


strs = ["blw", "bwl", "wlb"]
print(Solution().numSimilarGroups(strs))
