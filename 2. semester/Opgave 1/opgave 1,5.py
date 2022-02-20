tal = [10,8,7,9,8,9,10,6,7,8,11,3,4,17]
print("Vi har en liste her, som vi vil finde de 10 første tal af: ", tal)

def cut10(a):
    x = slice(10)

    c = a[x]
    return tuple(c)

for x in cut10(tal):
    print(x)