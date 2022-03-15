import cmath
sqrt = cmath.sqrt

print("Velkommen til en andengradslinjings hjælper")

a = float(input("Skriv a her (Husk det skal være et tal): "))
b = float(input("Skriv b her (Husk det skal være et tal): "))
c = float(input("Skriv c her (Husk det skal være et tal): "))

d = b * b - 4 * a * c
print(d)
while d <= 0:
    print("Det som du har skrevet giver ", d, "som er et minus tal. Derfor beder vi dig om at starte det igen")
    break

svar1 = (-b + sqrt(d)) / (2*a)
svar2 = (-b - sqrt(d)) / (2*a)

print("løsningen er ", svar1, " og ", svar2)
print("Ved svar kommer der +0j, bare inorerer det")