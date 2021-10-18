class Solution:
    def fairCandySwap(self, A: list, B: list) -> list:
        sum_a = sum(A)
        sum_b = sum(B)
        diff = (sum_a - sum_b)//2
        for a in A:
            if a-diff in B:
                return [a, a-diff]
