class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total_dresses = sum(machines)
        num_machines = len(machines)

        if total_dresses % num_machines:
            return -1

        avg = total_dresses // num_machines
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans
