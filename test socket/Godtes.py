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
print("5\n")

FPS = 60 #bestemmer maks fps. bare så det ikke ender med at lagge noget ud.

"""skt = socket.socket() #Forbinder til Rasp... Husk at tjekke om ip'en og porten er den rigtige

host = "192.168.1.249" # Ip-addressen for Raspberry Pi
port = 4200

skt.connect((host, port))
"""
def draw_windue(styr): #Her er noget styring til skærmen
    WIN.fill(skærmfarve) #Det her er baggrundsfarven
    WIN.blit(tar, (styr.x, styr.y)) #Bare et billede af et rat 
    pygame.display.update()

def main(): #Det vigtige kode er her
    styr = pygame.Rect(0, 0, 507, 676)

    clock = pygame.time.Clock()
    gameLoop = True
    while gameLoop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed() #Den her siger hvad der skal gøres, finds forskellige taster bliver trykket på
                if keys[pygame.K_w]:
                    print("12")
                elif keys[pygame.K_q]:
                    print("11")
                elif keys[pygame.K_e]:
                    print("13")
                elif keys[pygame.K_r]:
                    print("14")
                elif keys[pygame.K_a]:
                    print("20")
                elif keys[pygame.K_s]:
                    print("21")
                elif keys[pygame.K_d]:
                    print("23")
                elif keys[pygame.K_f]:
                    print("24")

        draw_windue(styr)
    pygame.quit()


if __name__ == "__main__":
    main()