n_list = []
x_list = []

while True:  # データセットの読み込み
    n, x = (int(y) for y in input().split())

    if (n == 0 and x == 0):
        break

    n_list.append(n)
    x_list.append(x)

count = [0] * len(n_list)

for i in range(len(n_list)):  # count[i]毎の処理を行う
    for a in range(1, n_list[i] + 1):  # 1 <= a <= n_list[i]に関して以下の処理を行う
        for b in range(a + 1, n_list[i] + 1):  # a < b <= n_list[i]に関して以下の処理を行う
            # b < c <= n_list[i]に関して以下の処理を行う
            for c in range(b + 1, n_list[i] + 1):
                if a + b + c == x_list[i]:
                    count[i] += 1

for i in count:
    print(i, end="")
