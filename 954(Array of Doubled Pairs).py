class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        num_dict = {}
        arr.sort()
        for num in arr:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        for num in arr:
            if num in num_dict:
                if num_dict[num] == 1:
                    num_dict.pop(num)
                else:
                    num_dict[num] -= 1

                if num >= 0 and 2 * num in num_dict:
                    if num_dict[2 * num] == 1:
                        num_dict.pop(2 * num)
                    else:
                        num_dict[2 * num] -= 1
                    continue

                if num < 0 and num % 2 == 0 and num // 2 in num_dict:
                    if num_dict[num // 2] == 1:
                        num_dict.pop(num // 2)
                    else:
                        num_dict[num // 2] -= 1
                    continue

                return False
        return True

num = [4,-2,2,-4]
print(Solution().canReorderDoubled(arr=num))