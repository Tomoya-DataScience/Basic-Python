a, b, c = (int(x) for x in input().split())
count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count += 1
print(count)
