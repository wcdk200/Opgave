#Det rigtige tal
ulla=5

angæt=3
while angæt >0:
    gud=input("Skriv et tal som du vil gætte på. Tallet er imellem 0 og 10: ")

    gød=float(gud)

    if gød == 5:
        print("Du gættede rigtigt")
        break
    elif gød > 5:
        print("Du gættede for højt")
        angæt = angæt - 1
    elif gød < 5:
        print("du gættede for lavt")
        angæt = angæt - 1
