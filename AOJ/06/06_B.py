from ast import Pass

max_rank = 13

n = int(input())

# 不足しているカードのリスト(rangeの範囲に注意)
list_S = list(range(1, max_rank + 1))
list_H = list(range(1, max_rank + 1))
list_C = list(range(1, max_rank + 1))
list_D = list(range(1, max_rank + 1))

# 入力をn回行って不足しているカードのリストから入力に一致するものを削除
for i in range(n):
    word = input().split()
    egara = word[0]
    rank = int(word[1])
    if egara == "S":
        if rank in list_S:
            list_S.remove(rank)
        else:
            Pass
    elif egara == "H":
        if rank in list_H:
            list_H.remove(rank)
        else:
            Pass
    elif egara == "C":
        if rank in list_C:
            list_C.remove(rank)
        else:
            Pass
    elif egara == "D":
        if rank in list_D:
            list_D.remove(rank)
        else:
            Pass

for s in list_S:
    print(f"S {s}")

for s in list_H:
    print(f"H {s}")

for s in list_C:
    print(f"C {s}")

for s in list_D:
    print(f"D {s}")
