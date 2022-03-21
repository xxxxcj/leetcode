from queue import Queue


class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        optimal_length2main = [-1 for _ in range(len(patience))]
        graph = {i: [] for i in range(len(patience))}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        q = Queue()
        q.put(0)
        optimal_length2main[0] = 0
        while not q.empty():
            v = q.get()
            for next in graph[v]:
                if optimal_length2main[next] == -1:
                    optimal_length2main[next] = optimal_length2main[v] + 1
                    q.put(next)

        max_l = 0
        for idx, l in enumerate(optimal_length2main):
            if idx == 0:
                continue
            if 2*l < patience[idx]:
                max_l = max(max_l, 2*l)
            else:
                if 2*l % patience[idx] == 0:
                    m = (2*l // patience[idx] - 1) * patience[idx] + 2*l
                else:
                    m = (2 * l // patience[idx]) * patience[idx] + 2 * l
                max_l = max(max_l, m)

        return max_l + 1


edges = [[0, 1], [1, 2]]
patience = [0, 2, 1]
sol = Solution()
print(sol.networkBecomesIdle(edges, patience))
