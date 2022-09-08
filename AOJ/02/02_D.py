W, H, x, y, r = (int(x) for x in input().split())
if (x >= r and r <= y and r <= H - y):  # 円が左に寄っているときの境界
    print("Yes")
elif (x <= W - r and r <= y and y <= H - r):  # 円が右に寄っているときの境界
    print("Yes")
else:
    print("No")
