class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """

        def compute_rect(ax1, ay1, ax2, ay2):
            return (ay2 - ay1) * (ax2 - ax1)

        def compute_y_of(x1: int, x2: int):
            y1 = []
            if ax1 <= x1 <= ax2:
                y1.append(ay1)
                y1.append(ay2)
            if bx1 <= x1 <= bx2:
                y1.append(by1)
                y1.append(by2)

            y2 = []
            if ax1 <= x2 <= ax2:
                y2.append(ay1)
                y2.append(ay2)
            if bx1 <= x2 <= bx2:
                y2.append(by1)
                y2.append(by2)
            return max(min(y1), min(y2)), min(max(y1), max(y2))

        if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
            return compute_rect(ax1, ay1, ax2, ay2) + compute_rect(bx1, by1, bx2, by2)

        top_points = [ax1, ax2, bx1, bx2]
        top_points.sort()

        area = 0
        y_min, y_max = compute_y_of(top_points[0], top_points[1])
        area += compute_rect(top_points[0], y_min, top_points[1], y_max)
        y_min, y_max = compute_y_of(top_points[1], top_points[2])
        area += compute_rect(top_points[1], y_min, top_points[2], y_max)
        y_min, y_max = compute_y_of(top_points[2], top_points[3])
        area += compute_rect(top_points[2], y_min, top_points[3], y_max)

        return area
    """
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea
    """

sol = Solution()
print(sol.computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
