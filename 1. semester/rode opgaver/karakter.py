karaa=input("Skriv din danske karaktere her: ")
kara=float(karaa)
print("din danske karaktere er: ", kara)

#Lortet vírker bare huskk at lave float
if kara > 10: 
    print("Din alfabet karaktere er A")
elif kara > 7: 
    print("Din alfabet karaktere er B")
elif kara > 4: 
    print("Din alfabet karaktere er C")
elif kara > 2: 
    print("Din alfabet karaktere er D")
elif kara > 0: 
    print("Din alfabet karaktere er E")
elif kara > -3: 
    print("Din alfabet karaktere er Fx")
elif kara == -3: 
    print("Din alfabet karaktere er F")
elif kara < -3: 
    print("Du er Fucked")