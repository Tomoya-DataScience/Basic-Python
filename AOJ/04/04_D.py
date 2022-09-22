def calc(n, list):
    # mapを使う
    print(min(list), max(list), sum(list))


n = int(input())
list = list(map(int, input().split()))

calc(n, list)
