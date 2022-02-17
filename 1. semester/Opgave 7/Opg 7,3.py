al=input("Skriv det antal år du har levet her og et ord kommer frem: ")

ak=float(al)

if ak <= 12:
    print("Haha du bare et barn")
elif ak >=13 and ak <= 17:
    print("Du næsten voksen er din lille teenager")
elif ak >=18 and ak <=64:
    print("Du en voksen nu tillykke")
elif ak >=65:
    print("Nu burde du bare gå på pension og nyde dit liv")
