list = []

while (1):
    x = int(input().split(sep="\n"))
    if x == 0:
        break
    list.append(x)
for i in range(len(list)):
    print(f"Case {i + 1}: {list[i]}")
