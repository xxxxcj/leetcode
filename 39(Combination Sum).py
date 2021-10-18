class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        min = candidates[0]
        for i in candidates:
            if i < min:
                min = i
        ans = []

        def get_combination_sum(target, elements:list, index):
            for i in range(index, len(candidates)):
                if target - candidates[i] == 0:
                    new = elements.copy()
                    new.append(candidates[i])
                    ans.append(new)
                elif target - candidates[i] < min:
                    pass
                else:
                    new = elements.copy()
                    new.append(candidates[i])
                    get_combination_sum(target - candidates[i], new, i)

        get_combination_sum(target, [], 0)

        return ans


candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates,target))

