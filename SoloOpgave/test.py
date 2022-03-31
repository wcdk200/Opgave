#se hvilken type en ting er (str,float osv.)
print(type("u"))
#Hvilken ord vi ikke må bruge
import keyword
print(keyword)
#clear ting... men virker ikke helt
import os
clear = lambda: os.system("cls")
print("hej")