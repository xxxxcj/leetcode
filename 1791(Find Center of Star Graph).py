class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        node_degree = {}
        for e in edges:
            if e[0] not in node_degree:
                node_degree[e[0]] = 1
            else:
                node_degree[e[0]] += 1
            if e[1] not in node_degree:
                node_degree[e[1]] = 1
            else:
                node_degree[e[1]] += 1

        max_key = -1
        max_degree = -1
        for key in node_degree:
            if max_degree < node_degree[key]:
                max_degree = node_degree[key]
                max_key = key

        return max_key