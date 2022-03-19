class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        list1_dict, list2_dict = {}, {}
        for idx, item in enumerate(list1):
            list1_dict[item] = idx
        for idx, item in enumerate(list2):
            list2_dict[item] = idx

        ans = []
        min_idx = len(list1) + len(list2)
        for idx, pos in enumerate(list1):
            if pos in list2_dict:
                if idx + list2_dict[pos] < min_idx:
                    min_idx = idx + list2_dict[pos]
                    ans = [pos]
                elif idx + list2_dict[pos] == min_idx:
                    ans.append(pos)

        return ans