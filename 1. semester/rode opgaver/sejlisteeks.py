# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:39:04 2018

Eksempler med lister og exception handling

Dette program beder brugeren lave en liste.

Derefter skal brugeren finde elementer fra listen med indeksering.

Hvis indeks ikke passer med listen, skal programmet reagere med 
en exception

@author: HTH
"""

# Beder brugeren om input om hvor mange elementer listen skal have
while True:
    try:
        antalElementer = int(input("Hvor mange elementer skal listen have? "))
        break
    except ValueError:
        print("Skriv venlist et tal din dompap")

elementListe = []

# Brugeren skal fylde listen op med elementer
for elementIndeks in range(antalElementer):
    element = input("Indtast element nr. " + str(elementIndeks) +" som skal i listen: ")
    elementListe.append(element)
    
# Brugeren skal nu finde elementer frem fra listen
while True:
    elementIndeks = input("Vælg indeks fra listen, mellem 0 og " + str(antalElementer-1) + ". Vælg q for at stoppe. ")
    if elementIndeks == "q" or elementIndeks == "Q":
        break
    
    try:
        element = elementListe[int(elementIndeks)]
    except IndexError:
        print("Indeks " + str(elementIndeks) + " er ikke i listen.")
    except ValueError:
        print("Din kræft idiot du skal bare skrive q for at stoppe eller et tal imellem 0 og " + str(antalElementer))
    else:
        print("Element på plads " + str(elementIndeks) + " i listen er " + str(elementListe[int(elementIndeks)]))