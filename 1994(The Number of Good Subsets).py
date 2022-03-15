from queue import Queue


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        num_dict = {
            1: {1},
            2: {2},
            3: {3},
            4: -1,
            5: {5},
            6: {2, 3},
            7: {7},
            8: -1,
            9: -1,
            10: {2, 5},
            11: {11},
            12: -1,
            13: {13},
            14: {2, 7},
            15: {3, 5},
            16: -1,
            17: {17},
            18: -1,
            19: {19},
            20: -1,
            21: {3, 7},
            22: {2, 11},
            23: {23},
            24: -1,
            25: -1,
            26: {2, 13},
            27: -1,
            28: -1,
            29: {29},
            30: {2, 3, 5}
        }

        ans = -1
        q = Queue()
        q.put([])

        def Union(a: set, b: set):
            if len(a.intersection(b)) != 0:
                return set(), False
            else:
                return a.union(b), True

        for i in range(len(nums)):
            for j in range(2 ** i):
                p: list = q.get()
                q.put(p.copy())
                p.append(nums[i])
                q.put(p.copy())

        while not q.empty():
            ans += 1
            p = q.get()
            if p == [1]:
                ans -= 1
            s = set()
            for i in p:
                if num_dict[i] != -1:
                    s, flag = Union(s, num_dict[i].copy())
                    if not flag:
                        ans -= 1
                        break
                else:
                    ans -= 1
                    break

        return ans % (10 ** 9 + 7)


nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().numberOfGoodSubsets(nums))
