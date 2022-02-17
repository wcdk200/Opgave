import socket, time

print("Kører klienten\n")

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Laver en socket

host = "192.168.1.249" # Dette er IP-adressen for Raspberry Pi
port = 4200

# Definerer data:
dataListe = ["Fister", "medister", "poelse", "dit", "lokum"]

# Sender data
for data in dataListe:
    print("Sender data:", str(data))
    
    # Indkoder data til UTF-8
    indkodet_data = data.encode("UTF-8")
    skt.sendto(indkodet_data, (host, port))

    time.sleep(1)
        
skt.close() # Lukker forbindelsen

print("Socketen blev lukket")