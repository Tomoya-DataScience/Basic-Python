def calc(a, op, b):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)


while (1):
    list = input().split()
    a = int(list[0])
    op = list[1]
    b = int(list[2])
# while文の外で計算すると入力を複数受け取れる
    if op == "?":
        break

    calc(a, op, b)
