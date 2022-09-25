class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        group_size_dict = {}
        for idx, group_size in enumerate(groupSizes):
            if group_size not in group_size_dict:
                group_size_dict[group_size] = [idx]
            else:
                group_size_dict[group_size].append(idx)

        ans = []
        for key in group_size_dict.keys():
            for i in range(len(group_size_dict[key]) // key):
                ans.append(group_size_dict[key][key * i:key * (i + 1)])
        return ans


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(Solution().groupThePeople(groupSizes))
