class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)

        t = m // n

        if t < 1:
            for i in range(n):
                flag = True
                for j in range(m):
                    if b[j] != a[(i + j) % n]:
                        flag = False
                        break
                if flag:
                    return 1 + int((i + m) > n)
            return -1

        for i in range(1, t):
            if b[0:n] != b[i * n: (i + 1) * n]:
                return -1

        for i in range(len(b[t*n:])):
            if b[t*n + i] != b[i]:
                return -1

        def is_equ(i):
            for j in range(n):
                if a[j] != b[(i + j) % n]:
                    return False
            return True

        for i in range(n):
            if is_equ(i):
                return int(i != 0) + (m - i) // n + int((m - i) % n != 0)
        return -1


a = "abcabcabcabc"
b = "abac"
sol = Solution()
print(sol.repeatedStringMatch(a,b))
