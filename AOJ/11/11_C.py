class Dice:
    def __init__(self, array):
        self.top = array[0]  # 上面
        self.front = array[1]  # 正面
        self.right = array[2]  # 右の面
        self.left = array[3]  # 左の面
        self.back = array[4]  # 背面
        self.under = array[5]

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

    def spin_right(self):  # 上面から見て右周りに90度回転
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
                for _ in range(4):  # 360度回転させる
                    if self.same_place(array):
                        same_flag = True
                    self.spin_right()
                self.roll_N()
            self.spin_right()
            self.roll_S()
        return same_flag


roll_1 = list(map(int, input().split()))  # 1つ目のサイコロの面の入力を受け取る
roll_2 = list(map(int, input().split()))  # 2つ目のサイコロの面の入力を受け取る

dice_1 = Dice(roll_1)

if dice_1.same_dice(roll_2):
    print("Yes")
else:
    print("No")
