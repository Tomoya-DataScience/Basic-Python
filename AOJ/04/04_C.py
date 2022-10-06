def calc(a_list, op_list, b_list):
    for i in range(len(a_list)):
        if op_list[i] == "+":
            print(a_list[i] + b_list[i])
        elif op_list[i] == "-":
            print(a_list[i] - b_list[i])
        elif op_list[i] == "*":
            print(a_list[i] * b_list[i])
        elif op_list[i] == "/":
            print(a_list[i] // b_list[i])


a_list = []
b_list = []
op_list = []

while (1):
    list = input().split()
    if list[1] == "?":
        break
    else:
        op_list.append(list[1])
    a_list.append(int(list[0]))
    b_list.append(int(list[2]))
# while文の外で計算すると入力を複数受け取れる

calc(a_list, op_list, b_list)
