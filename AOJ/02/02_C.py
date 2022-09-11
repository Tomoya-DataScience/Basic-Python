a, b, c = (int(x) for x in input().split())
answer = sorted([a, b, c])
print(f"{answer[0]} {answer[1]} {answer[2]}")
