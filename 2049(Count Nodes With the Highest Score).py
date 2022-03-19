class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        node_score = [0 for _ in range(len(parents))]
        children = [[] for _ in range(len(parents))]
        for idx, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(idx)

        def compute_node_score(i):
            node_score[i] += 1
            for child in children[i]:
                node_score[i] += compute_node_score(child)
            return node_score[i]

        compute_node_score(0)

        print(node_score)

        remove_score = []
        for i in range(len(parents)):
            score = 1
            if i != 0:
                score *= node_score[0] - node_score[i]

            if len(children[i]) != 0:
                for child in children[i]:
                    score *= node_score[child]

            remove_score.append(score)

        max_val = 0
        max_count = 0
        for val in remove_score:
            if val > max_val:
                max_val = val
                max_count = 1
            elif val == max_val:
                max_count += 1

        return max_count


parents = [-1, 2, 0, 2, 0]
sol = Solution()
print(sol.countHighestScoreNodes(parents))
