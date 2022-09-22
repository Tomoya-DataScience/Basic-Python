large_list = []  # 小さい方の値を入れるリスト
small_list = []  # 大きい方の値を入れるリスト
while (1):
    x, y = (int(i) for i in input().split())
    if x == 0 and y == 0:
        break
    if x >= y:
        small_list.append(x)
        large_list.append(y)
    else:
        large_list.append(x)
        small_list.append(y)

for i in range(len(large_list)):
    print(large_list[i], small_list[i])
