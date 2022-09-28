n = int(input())
list = list(map(int, input().split()))

for i in range(len(list)):
    print(list[len(list) - 1 - i], end=" ")
