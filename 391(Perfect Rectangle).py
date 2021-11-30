from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)
        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]
            area += (a - x) * (b - y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[(minX, maxY)] != 1 or cnt[
            (maxX, minY)] != 1 or cnt[(maxX, maxY)] != 1:
            return False

        del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        return all(c == 2 or c == 4 for c in cnt.values())

rectangles = [[0,9997,1,9998],[0,9998,1,9999]]
sol = Solution()
print(sol.isRectangleCover(rectangles))
