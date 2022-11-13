class Dice:
    def __init__(self, array):
        self.top = array[0]  # 上面
        self.front = array[1]  # 正面
        self.right = array[2]  # 右の面
        self.left = array[3]  # 左の面
        self.back = array[4]  # 背面
        self.under = array[5]  # 下面

    def roll_S(self):  # S(手前側)方向への回転
        self.top, self.front, self.back, self.under =\
            self.back, self.top, self.under, self.front

    def roll_N(self):  # N(奥側)方向への回転
        self.top, self.front, self.back, self.under =\
            self.front, self.under, self.top, self.back

    def roll_W(self):  # W(左)方向への回転
        self.top, self.right, self.left, self.under =\
            self.right, self.under, self.top, self.left

    def roll_E(self):  # E(右)方向への回転
        self.top, self.right, self.left, self.under =\
            self.left, self.top, self.under, self.right

    def spin_right(self):
        self.right, self.front, self.left, self.back =\
            self.back, self.right, self.front, self.left

    def same_place(self, array):  # 面の配置が同じかどうか判定するメソッド
        if self.top == array[0] and self.front == array[1] and self.right == array[2] and \
                self.left == array[3] and self.back == array[4] and self.under == array[5]:
            return True

    def same_dice(self, array):  # 同じサイコロかどうか判定するメソッド
        same_flag = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.same_place(array):
                        same_flag = True
                    self.spin_right()
                self.roll_N()
            self.spin_right()
            self.roll_S()
        return same_flag


n = int(input())
roll_list = [None] * n

for i in range(n):
    roll_list[i] = list(map(int, input().split()))

all_different_flag = True  # 全てのサイコロが異なっていればTrueを返すフラグ変数

for i in range(n - 1):
    for j in range(i + 1, n):
        dice = Dice(roll_list[i])
        if dice.same_dice(roll_list[j]):
            all_different_flag = False
            print("No")  # 同じサイコロが1組以上ある場合Noを出力
            break
        else:
            continue

if all_different_flag:
    print("Yes")
