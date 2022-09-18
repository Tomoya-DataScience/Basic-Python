import math


def circle(r):
    print(math.pi * r * r, 2 * math.pi * r)
# *でアンパックが出来る


r = int(input())

circle(r)
