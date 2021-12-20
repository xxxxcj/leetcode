import math


class Solution:
    def visiblePoints(self, points: list, angle: int, location: list) -> int:
        point2location_angles = list()
        same_as_location = 0
        for point in points:
            if point == location:
                same_as_location += 1
            else:
                point2location_angle = math.atan2((point[1] - location[1]), (point[0] - location[0]))
                point2location_angles.append(point2location_angle)
        point2location_angles.sort()
        print(point2location_angles)

        start, stop = 0, 0
        max_visible_num = 0
        visible_num = 0
        angle += 0.0005
        while start < len(point2location_angles):
            if (point2location_angles[stop] - point2location_angles[start]) % (2*math.pi) <= angle * math.pi / 180:
                stop = (stop + 1) % len(point2location_angles)
                visible_num += 1
                if visible_num > max_visible_num:
                    max_visible_num = visible_num
                    if max_visible_num == len(point2location_angles):
                        break
            else:
                start += 1
                visible_num -= 1

        return max_visible_num + same_as_location


points = [[30, 48], [26, 26], [82, 91], [63, 7], [3, 65], [74, 0], [12, 26], [12, 46], [57, 1], [32, 17], [96, 37],
          [21, 54], [20, 47], [88, 61], [88, 44], [69, 18], [21, 50], [23, 42], [48, 43], [9, 93], [45, 81], [43, 58],
          [14, 82], [92, 63], [16, 33], [49, 34], [57, 50], [59, 91], [59, 61], [13, 80], [21, 81], [3, 56], [30, 85],
          [70, 94], [59, 27], [56, 15], [4, 50], [30, 11], [45, 82], [87, 49], [12, 24], [93, 37], [20, 38], [53, 76],
          [28, 25], [65, 93], [31, 86], [25, 50], [63, 60], [79, 48], [73, 58], [76, 63], [99, 43], [17, 45], [53, 9],
          [99, 38], [10, 31], [14, 22], [30, 53], [34, 88], [37, 59], [66, 86], [87, 58], [100, 15], [48, 0], [55, 31],
          [50, 19], [96, 32], [40, 79], [46, 45], [73, 47], [74, 28], [72, 66], [35, 42], [6, 89], [62, 49], [67, 42],
          [80, 47], [82, 31], [8, 96], [97, 59], [36, 65], [31, 48], [69, 11], [12, 25], [68, 56], [39, 62], [37, 8],
          [58, 36], [5, 56], [99, 94], [80, 94], [64, 70], [80, 61], [76, 47], [78, 67], [41, 70], [85, 60], [15, 40],
          [40, 50], [20, 44], [87, 32], [55, 90], [33, 76], [76, 65], [49, 50], [51, 10], [70, 76], [1, 28]]
angle = 180
location = [52, 19]
sol = Solution()
print(sol.visiblePoints(points, angle, location))
