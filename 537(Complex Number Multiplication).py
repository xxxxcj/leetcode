class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_list = num1.split('+')
        num2_list = num2.split('+')

        real1 = int(num1_list[0])
        real2 = int(num2_list[0])
        imaginary1 = int(num1_list[1][:-1])
        imaginary2 = int(num2_list[1][:-1])

        real = real1*real2 - imaginary1*imaginary2
        imaginary = real1 * imaginary2 + real2 * imaginary1

        return str(real) + '+' + str(imaginary) + 'i'