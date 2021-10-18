class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        min = candidates[0]
        for i in candidates:
            if i < min:
                min = i
        ans = []

        candidates.sort()

        def get_combination_sum(target, elements:list, index):
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] == 0:
                    new = elements.copy()
                    new.append(candidates[i])
                    ans.append(new)
                elif target - candidates[i] < min:
                    pass
                else:
                    new = elements.copy()
                    new.append(candidates[i])
                    get_combination_sum(target - candidates[i], new, i + 1)

        get_combination_sum(target, [], 0)

        return ans


candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))

