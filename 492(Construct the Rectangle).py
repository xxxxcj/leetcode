import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        n = int(math.sqrt(area))
        for i in range(n, 0, -1):
            if area % i == 0:
                return [area // i, i]
