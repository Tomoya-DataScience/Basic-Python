W, H, x, y, r = (int(x) for x in input().split())
if (r <= x and x <= W - r and r <= y and y <= H - r):
    print("Yes")
else:
    print("No")
