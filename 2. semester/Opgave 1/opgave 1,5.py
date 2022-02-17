l = [10,8,7,9,8,9,10,6,7,8,11,3,4,17]
print("Vi har en liste her, som vi vil finde de 10 første tal af: ", l)

def cut10():
    x = slice(10)
    lt = (l[x])
    tt = tuple(lt)
    print("De første 10 tal er: ",tt)

cut10()