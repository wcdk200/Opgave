b = 0

while 1:
    if b == 63:
        b = b + 6
        print(b)
    elif b == 99:
        print(b)
        print("Færdig")
        break
    elif b == 0:
        b = b +3
        print(b)
    elif b > 0:
        b = b + 3
        print(b)

