info = [[[0] * 10 for i in range(3)] for j in range(4)]  # 入居者の情報を格納する配列

n = int(input())

for info in range(n):  # infoは情報のindex
    b, f, r, v = (int(x) for x in input().split())
    info[b - 1][f - 1][r - 1] += v  # 多次元リストのindexが0から始まることに注意

for building in range(4):
    for floor in range(3):
        for r in range(10):
            print(f" {info[building][floor][r]}", end="")
        print("\n")
    if building < 3:
        for j in range(20):
            print("#", end="")
        print("\n")
