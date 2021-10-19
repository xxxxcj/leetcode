import math


def D(x):
    if math.floor(x) <= 1:
        return 1
    else:
        return 3 * D(x / 4) + x - 2


def new_D(x):
    if math.floor(x) <= 1:
        return 1
    else:
        y = 1
        n = math.floor(math.log(x / 2, 4)) + 1
        for i in range(n):
            y += (3 / 4) ** i * x
        return y


x = 1000
for i in range(x):
    x1 = D(i)
    x2 = new_D(i)
    if abs(x1 - x2) < 0.0001:
        print(True)
    else:
        print(False)


def test(i: [int]) -> int:
    return i


print(float('inf'))
print(int(10 / -11))
print(bin())