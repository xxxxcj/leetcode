class Solution:
    def isNumber(self, s: str) -> bool:
        point_pos, e_pos, num_pos = -1, -1, []

        for idx, item in enumerate(s):
            if ord('0') <= ord(item) <= ord('9'):
                num_pos.append(idx)
            elif item == '+' or item == '-':
                if idx != e_pos+1:
                    return False
            elif item == 'e' or item == 'E':
                if e_pos != -1:
                    return False
                else:
                    e_pos = idx
            elif item == '.':
                if point_pos != -1:
                    return False
                else:
                    point_pos = idx
            else:
                return False

        if len(num_pos) == 0 or ((e_pos < num_pos[0] or e_pos > num_pos[-1]) and e_pos != -1):
            return False
        if point_pos <= e_pos or e_pos == -1 or point_pos == -1:
            return True
        return False


test =['e']
for i in test:
    print(Solution().isNumber(i))
