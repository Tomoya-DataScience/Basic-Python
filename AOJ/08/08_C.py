alphabet_num = 26
count = [0] * alphabet_num

all_input = ""
while True:
    input_line = input()
    if input_line:
        all_input = all_input + input_line
    else:
        break
# 改行を含む文字列の入力方法は？


for c in all_input:
    for i in range(alphabet_num):
        if c == chr(ord('A') + i) or c == chr(ord('a') + i):
            count[i] += 1

for i in range(alphabet_num):
    print(f"{chr(ord('a') + i)} : {count[i]}")
