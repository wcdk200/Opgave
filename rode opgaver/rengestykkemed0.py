aa = input("Skriv et tal ")
bb = input("skriv et tal ")

a = float(aa)
b = float(bb)

try:
    result = a/b
except ZeroDivisionError:
    print("Du ik div med 0")
else:
    print(result)
