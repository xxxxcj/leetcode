class Solution:
    def countBits(self, num: int) -> list:
        # 000 001 010 011
        # 100 101 110 111

        bits = [0]
        hightBit = 0

        for i in range(1, num):
            if i & (i-1) == 0:
                hightBit = i
            bits.append(bits[i - hightBit] + 1)
        return bits
