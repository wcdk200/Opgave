import time
import pygame
import socket

tar = pygame.image.load("Opgave/test socket/sjovTing.png") #Sejt sådan impoterer man et billede

#Det er længden og højden på winduet som popper op når programet køre
WIDTH, HEIGHT = 900, 743

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Motorstyring") #Det er navnet på programet

#siger lidt sig selv, men det er baggrundsfarven på vores windue(farven står i RGB)
skærmfarve = (0, 255, 185)

print("Kører klienten\n")

FPS = 60 #bestemmer maks fps. bare så det ikke ender med at lagge noget ud.

skt = socket.socket() #Forbinder til Rasp... Husk at tjekke om ip'en og porten er den rigtige

host = "192.168.1.249" #Ip-addressen for Raspberry Pi
port = 4200 #og ja det her er porten

skt.connect((host, port))
"""
frem = 100,75
højre = 100, 0
lhøjre = 100, 55
venster = 0,75
lvenster = 80,75
stop = 0,0
"""

def draw_windue(styr): #Her er noget styring til skærmen
    WIN.fill(skærmfarve) #Det her er baggrundsfarven
    WIN.blit(tar, (styr.x, styr.y)) #Bare et billede af et rat 
    pygame.display.update()

def main(): #Det vigtige kode er her
    styr = pygame.Rect(195, 0, 507, 676)

    w = False
    a = False
    s = False
    d = False
    frem = False
    højre = False
    lhøjre = False
    venster = False
    lvenster = False
    stop = False

    clock = pygame.time.Clock()
    gameLoop = True
    while gameLoop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key = pygame.key.get_pressed()
                if event.key == pygame.K_w:
                    w = True
                
                if event.key == pygame.K_a:
                    a= True

                if event.key == pygame.K_s:
                    s = True

                if event.key == pygame.K_d:
                    d = True
                else:
                    w = False
                    a = False
                    s = False
                    d = False
            
            if w == True:
                frem = True
            if a == True:
                venster = True
            if s == True:
                stop = True
            if d == True:
                højre = True

            if frem == True:
                data = "100,75" #V sendes først også H muligvis den anden vej rundt
                nyt_data = data.encode("UTF-8")
                skt.sendall(nyt_data)
            if venster == True:
                data = "0,100"
                nyt_data = data.encode("UTF-8")
                skt.sendall(nyt_data)
            if stop == True:
                data = "0,0"
                nyt_data = data.encode("UTF-8")
                skt.sendall(nyt_data)
            if højre == True:
                data = "100,0"
                nyt_data = data.encode("UTF-8")
                skt.sendall(nyt_data)

        draw_windue(styr)
    pygame.quit()

if __name__ == "__main__":
    main()
