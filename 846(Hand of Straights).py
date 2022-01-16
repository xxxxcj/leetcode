import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        stk = list()
        for item in hand:
            heapq.heappush(stk, item)

        while len(stk) != 0:
            i = groupSize
            group = []
            tmp = []
            while i > 0:
                if i == groupSize:
                    group.append(heapq.heappop(stk))
                    i -= 1
                else:
                    if len(stk) > 0:
                        item = heapq.heappop(stk)
                    else:
                        return False

                    if item == group[-1]:
                        tmp.append(item)
                    elif item == group[-1] + 1:
                        group.append(item)
                        i -= 1
                    else:
                        return False

            for i in tmp:
                heapq.heappush(stk, i)

        return True


hand = [1, 2, 3, 4, 5, 6, 7, 8]
groupSize = 4
sol = Solution()
print(sol.isNStraightHand(hand, groupSize))
