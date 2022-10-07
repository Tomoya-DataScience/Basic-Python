n_list = []

while True:
    n = int(input())
    if n == 0:
        break
    n_list.append(n)

for i in range(len(n_list)):
    s = str(n_list[i])
    # 1文字ずつ数値化し配列にする
    array = list(map(int, s))
    # 合計値を出力
    print(sum(array))
