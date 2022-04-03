class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])

        new_img = [[0 for _ in range(n)] for _ in range(m)]

        surrounding_i = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        surrounding_j = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        for i in range(m):
            for j in range(n):
                pixel_sum = 0
                count = 0
                for idx in range(9):
                    s_i = i + surrounding_i[idx]
                    s_j = j + surrounding_j[idx]
                    if 0 <= s_i < m and 0 <= s_j < n:
                        pixel_sum += img[s_i][s_j]
                        count += 1
                new_img[i][j] = pixel_sum // count

        return new_img


img = [[100, 200, 100],
       [200, 50, 200],
       [100, 200, 100]]
sol = Solution()
print(sol.imageSmoother(img))
