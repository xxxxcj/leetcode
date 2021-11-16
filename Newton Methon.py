from math import *


# def f(x):
#     return log(exp(x) + exp(-x), exp(1))
#
#
# def f_(x):
#     return (exp(x) - exp(-x)) / (exp(x) + exp(-x))
#
#
# def f__(x):
#     return 4 / pow(exp(x) + exp(-x), 2)

def f(x):
    return -log(x, exp(1)) + x


def f_(x):
    return -1 / x + 1


def f__(x):
    return 1 / (x * x)


t = 1  # step
x0 = 3

max_iter = 100
iter = 0

x_ = x0
while iter < max_iter:
    x = x_ - t * f_(x_) / f__(x_)
    print(iter, x_, x)
    x_ = x
    iter += 1
