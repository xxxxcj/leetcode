class Solution:
    def minSwapsCouples(self, row: list) -> int:
        held = [False] * (len(row) // 2)
        couples_num = 0

        def get_another(idx):
            if idx % 2:
                return idx - 1
            else:
                return idx + 1

        def count_cycle(i):
            if held[i // 2]:
                return 0
            held[i // 2] = True
            idx = row.index(get_another(row[get_another(i)]))
            return 1 + count_cycle(idx)

        for i in range(0, len(row), 2):
            if not held[i // 2]:
                if row[i + 1] == get_another(row[i]):
                    held[i // 2] = True
                else:
                    x = count_cycle(i) - 1
                    couples_num += x

        return couples_num


row = [1, 4, 0, 5, 8, 7, 6, 3, 2, 9]
print(Solution().minSwapsCouples(row))
