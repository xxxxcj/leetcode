class Solution:
    def makeConnected(self, n: int, connections: list) -> int:
        rested_nodes = list(range(n))

        if len(connections) < n-1:
            return -1

        # 查找节点node的根节点函数
        def find_root(node, parent):
            if parent[node] == -1:  # node节点的父节点就是它自己时，说明它自己就是根节点
                return node
            else:  # node的父节点不是就一层一层向上找父节点
                return find_root(parent[node], parent)

        # 合并两个节点x,y的函数, 该函数返回1表示成功合并，返回0表示合并失败。
        # 当合并的两个点正好在同一个集合里就会合并失败
        def union(x, y, parent, rank):
            # 分别找x,y节点的根
            x_root, y_root = find_root(x, parent), find_root(y, parent)

            # 两节点的根不同，可合并;两节点的根相同会形成环，不可合并
            if x_root == y_root:
                return 0
            else:
                # parent[x_root] = y_root 在拼接时不能直接拼接了，要加入rank比较
                if rank[x_root] > rank[y_root]:
                    parent[y_root] = x_root
                elif rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                else:  # 两个相等的情况时，一个作为另一个的父节点，作为父节点的的深度需增加
                    parent[x_root] = y_root
                    rank[y_root] += 1
                return 1

        parent = [-1 for _ in range(n)]
        rank = [0 for _ in range(n)]
        for connection in connections:
            union(connection[0], connection[1], parent, rank)
        count = -1
        for i in parent:
            if i == -1:
                count += 1
        return count


n = 11
c = [[1, 4], [0, 3], [1, 3], [3, 7], [2, 7], [0, 1], [2, 4], [3, 6], [5, 6], [6, 7], [4, 7], [0, 7], [5, 7]]

sol = Solution()
print(sol.makeConnected(n, c))
