S = int(input())
h = S // (60 * 60)
m = (S % (60 * 60)) // 60
s = S - h * 60 * 60 - m * 60
print(f"{h}:{m}:{s}")
