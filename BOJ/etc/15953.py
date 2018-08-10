from sys import stdin
Read = stdin.readline

T = int(Read())

for _ in range(T):
    a, b = map(int, Read().split())
    prices = 0

    if a == 1:
        prices += 5000000
    elif 2 <= a <= 3:
        prices += 3000000
    elif 4 <= a <= 6:
        prices += 2000000
    elif 7 <= a <= 10:
        prices += 500000
    elif 11 <= a <= 15:
        prices += 300000
    elif 16 <= a <= 21:
        prices += 100000
    else:
        prices += 0

    if b == 1:
        prices += 5120000
    elif 2 <= b <= 3:
        prices += 2560000
    elif 4 <= b <= 7:
        prices += 1280000
    elif 8 <= b <= 15:
        prices += 640000
    elif 16 <= b <= 31:
        prices += 320000
    else:
        prices += 0

    print(prices)