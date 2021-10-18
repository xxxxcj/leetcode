import math


class Solution:
    def numRabbits(self, answers: list) -> int:
        answers.sort()

        count = dict()

        for i in answers:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        ret = 0
        for key in count:
            ret += math.ceil(count[key] / (key + 1)) * (key + 1)

        return ret


answers = [10, 10, 10]
print(Solution().numRabbits(answers))