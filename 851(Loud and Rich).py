class Solution:
    def loudAndRich(self, richer: list, quiet: list) -> list:
        # [next: list, quietest]
        richer_dict = [[[], i] for i in range(len(quiet))]

        def compute(i, j):
            if quiet[richer_dict[i][1]] < quiet[richer_dict[j][1]]:
                richer_dict[j][1] = richer_dict[i][1]
            for k in richer_dict[j][0]:
                compute(i, k)

        for relation in richer:
            richer_dict[relation[0]][0].append(relation[1])

            for k in richer_dict[relation[0]][0]:
                compute(relation[0], k)

        return [i[1] for i in richer_dict]
        # 看成图，然后用深度优先搜索更优

richer = [[0, 1], [1, 2]]
quiet = [0, 2, 1]
sol = Solution()
print(sol.loudAndRich(richer, quiet))
