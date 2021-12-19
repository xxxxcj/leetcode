class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        clipped_m, clipped_n = m, n
        for op in ops:
            if op[0] < clipped_m:
                clipped_m = op[0]
            if op[1] < clipped_n:
                clipped_n = op[1]
        return clipped_m*clipped_n
