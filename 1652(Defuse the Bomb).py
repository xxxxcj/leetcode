class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        code_copy = [i for i in code]
        n = len(code)
        for i in range(n):
            num = 0
            if k > 0:
                for j in range(k):
                    num += code_copy[(i + j + 1) % n]
            elif k < 0:
                for j in range(0, k, -1):
                    num += code_copy[(i + j - 1) % n]
            code[i] = num
        return code


code = [2,4,9,3]
k = 0
print(Solution().decrypt(code, k))

