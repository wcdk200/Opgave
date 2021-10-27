import socket

print("Kører serveren\n")

host = "10.31.128.105" # Dette er IP-adressen for Raspberry Pi
port = 3000 # Husk at portnumre på 1024 og lavere er priviligerede

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Man kan give argumenter til denne (f.eks. om det skal være TCP eller UDP)
skt.bind((host, port)) # Tilskriver IP-adressen og porten til vores socket

while True:
    
    data, adresse = skt.recvfrom(64)
    dekodet_data = data.decode("UTF-8")
    
    if data:
        print("Data modtaget: ", str(dekodet_data))
    else:
        print("Ikke mere data.")
        break
    
skt.close()