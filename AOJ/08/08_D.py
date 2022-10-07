s = input()
p = input()

for i in range(len(s)):
    print(f"i = {i}")
    if i + len(p) <= len(s):  # 探索する文字列の末尾がsの末尾までの場合の処理
        if s[i: i + len(p)] == p:
            print("Yes")
            break
    else:  # 末尾まで探索した場合先頭の文字列と結合
        if s[i:] + s[: i + len(p) - len(s)] == p:
            print("Yes")
            break
    if i == len(s) - 1:  # 探索する文字列の最初がsの末尾だった場合見つからなかったので探索を終了
        print("No")
