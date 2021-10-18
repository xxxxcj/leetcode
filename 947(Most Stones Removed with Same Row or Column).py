class Solution:
    def removeStones(self, stones: list) -> int:
        is_removed = [False for _ in range(len(stones))]

        def BFS(idx):
            result = 0
            stone = stones[idx]
            is_removed[idx] = True
            for i, item in enumerate(stones):
                if not is_removed[i] and (stone[0] == item[0] or stone[1] == item[1]):
                    result += BFS(i) + 1
            return result

        result = 0
        for idx, _ in enumerate(stones):
            if not is_removed[idx]:
                result += BFS(idx)
        return result


stones = [[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]
sol = Solution()
print(sol.removeStones(stones))
