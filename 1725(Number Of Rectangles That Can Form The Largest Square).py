class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        square_len = []
        max_len = 0
        for rect in rectangles:
            len = min(rect)
            if len > max_len:
                max_len = len
            square_len.append(len)

        ans = 0
        for len in square_len:
            if len == max_len:
                ans += 1

        return ans
