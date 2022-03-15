class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        if 2 * time > len(security) - 1:
            return []

        if time == 0:
            return list(range(len(security)))

        nonincreasing_list = []
        nondecreasing_list = []
        for i in range(len(security) - 1):
            if security[i] >= security[i + 1]:
                if len(nonincreasing_list) == 0:
                    nonincreasing_list.append([i, i + 1])
                elif nonincreasing_list[-1][1] == i:
                    nonincreasing_list[-1][1] = i + 1
                else:
                    nonincreasing_list.append([i, i + 1])

            if security[i] <= security[i + 1]:
                if len(nondecreasing_list) == 0:
                    nondecreasing_list.append([i, i + 1])
                elif nondecreasing_list[-1][1] == i:
                    nondecreasing_list[-1][1] = i + 1
                else:
                    nondecreasing_list.append([i, i + 1])

        nonincreasing = [-1 for _ in range(len(security))]
        nondecreasing = [-1 for _ in range(len(security))]

        for i in nonincreasing_list:
            for j in range(i[0], i[1] + 1):
                nonincreasing[j] = i[1]

        for i in nondecreasing_list:
            for j in range(i[0], i[1] + 1):
                nondecreasing[j] = i[1]

        ans = []
        for t in range(len(security) - 2 * time):
            if nonincreasing[t] != -1 and nonincreasing[t] >= time + t \
                    and nondecreasing[time + t] != -1 and nondecreasing[time + t] >= 2 * time + t:
                ans.append(time + t)

        return ans


security = [77,9,111,138,139,183,112,127,38,123,198,86,163,50,140,106,99,140,152,176,124,181,14,113,53,186,76,165,32,26,137,4,186,193,130,157,173,52,27,101,154,129,34,200,51,184,127,147,197,151,190,95,62,182,77,34,174,162,7,84,105,103,128]
time = 2
print(security[55-2:55+3])
sol = Solution()
print(sol.goodDaysToRobBank(security, time))
