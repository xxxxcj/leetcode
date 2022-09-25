class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        arr_dict = {}
        for idx, item in enumerate(arr):
            arr_dict[item] = idx

        for p in pieces:
            idx = []
            for num in p:
                if num not in arr_dict:
                    return False
                else:
                    if len(idx) == 0:
                        idx.append(arr_dict[num])
                    else:
                        if arr_dict[num] != idx[-1] + 1:
                            return False
                        idx.append(arr_dict[num])
        return True


arr = [37, 69, 3, 74, 46]
pieces = [[37, 69, 3, 74, 46]]
print(Solution().canFormArray(arr, pieces))
