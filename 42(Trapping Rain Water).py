class Solution:
    def trap(self, height: list) -> int:
        if len(height) == 0:
            return 0

        water_line = [None for x in range(len(height))]

        i, j, p1, p2 = 0, len(height) - 1, 0, len(height) - 1
        max_height_left, max_height_right = 0, 0
        while i < len(height):
            if max_height_left < height[i]:
                water_line[i] = height[i]
                max_height_left = height[i]
                p1 = i
            else:
                water_line[i] = max_height_left
            i += 1

        while j > p1:
            if max_height_right < height[j]:
                water_line[j] = height[j]
                max_height_right = height[j]
                p2 = j
            else:
                water_line[j] = max_height_right
            j -= 1

        if water_line[p1] < water_line[p2]:
            k = p1
            while k < p2:
                water_line[k] = water_line[p1]

        ans = 0
        for i in range(len(height)):
            if water_line[i] > height[i]:
                ans += water_line[i] - height[i]

        return ans


height = []
print(Solution().trap(height))
