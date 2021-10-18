import functools


class Solution:
    def largestNumber(self, nums: list) -> str:
        new_nums = list()
        for i in nums:
            num_list = list()
            if i == 0:
                num_list.append(i)
            while i != 0:
                num_list.append(i % 10)
                i //= 10
            new_nums.append(num_list)

        def cmp(a: list, b: list):
            if a == b:
                return 0
            i, j = len(a) - 1, len(b) - 1
            while i != -1 or j != -1:
                i %= len(a)
                j %= len(b)
                if a[i] > b[j]:
                    return -1
                elif a[i] < b[j]:
                    return 1
                else:
                    i -= 1
                    j -= 1

            return 0

        new_nums.sort(key=functools.cmp_to_key(cmp))
        print(new_nums)
        ret = ""

        for i in new_nums:
            for j in range(len(i) - 1, -1, -1):
                ret += str(i[j])

        if ret[0] == '0':
            i = 0
            while i < len(ret) and ret[i] == '0':
                i += 1

            ret = ret[i - 1:]
        return ret


nums = [3,43,48,94,85,33,64,32,63,66]

print(Solution().largestNumber(nums))
