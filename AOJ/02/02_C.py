a, b, c = (int(x) for x in input().split())
if (a < b):
    if (a < c):  # a < c < bのとき
        b, c = c, b
    elif (c < a):  # c < a < bのとき
        a, b, c = c, a, b
else:  # b <= aのとき
    if (a < c):  # b <= a < cのとき
        a, b = b, a
    elif (c < a):  # b <= c < aのとき
        a, b, c = b, c, a
    else:  # c < b <= aのとき
        a, b, c = c, a, b
print(f"{a} {b} {c}")
