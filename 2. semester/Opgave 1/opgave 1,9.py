from tkinter import N


maaling = open("C:/Users/sebgu/Desktop/Programmering/Opgave/2. semester/Opgave 1/opgave1,9.txt", "r")  #Af en eller anden grund skal jeg skrive helevejen ind til tekst filen. Så husk lige at ændre det
content = maaling.read()

contentList = content.split(",")
maaling.close()
print(contentList)
#Ved ik helt hvordan man skal kunne finde gennemsnitten imellem målingerne