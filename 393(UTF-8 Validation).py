class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        def get_uft8_length(a: int):
            if not (a >> 7) % 2:
                return 1
            else:
                if (a >> 6) % 2:
                    if not (a >> 5) % 2:
                        return 2
                    else:
                        if not (a >> 4) % 2:
                            return 3
                        else:
                            if not (a >> 3) % 2:
                                return 4
            return -1

        i = 0
        while i < len(data):
            length_utf8 = get_uft8_length(data[i])
            if length_utf8 == -1:
                return False
            else:
                if i + length_utf8 <= len(data):
                    for j in range(i + 1, i + length_utf8):
                        if (data[j] >> 6) != 2:
                            return False
                i += length_utf8

        return i == len(data)


sol = Solution()
data = [235, 140, 0b10111111, 0b0]
print(sol.validUtf8(data))
