import socket
import pygame
import time
"""
from pygame import image
from unifem import scale_image, blit_rotate_center

pygame.init()
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Motorstyring")

RAT_BIL = pygame.image.load("SejtTinnnger.jpg")
Win = pygame.image.load("biggGAl")

class AbstractCar:
    IMGGG = RAT_BIL

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMGGG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self, Win):
        blit_rotate_center(Win, self.img, (self.x, self.y), self.angle)

class PlayerCar(AbstractCar):
    IMG = RAT_BIL
    START_POS = (180, 200)   

def draw(Win, images, player_car):
    for img, pos in image:
        Win.blit(img, pos)
    
    player_car.draw(Win)
    pygame.display.update()
"""
gameLoop = True
#Player_Car = PlayerCar(4, 4)

skt = socket.socket()

host = "192.168.1.249" # Ip-addressen for Raspberry Pi
port = 4200

skt.connect((host, port))

while gameLoop:
    #draw(Win, image, Player_Car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            data = "17"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            data = "18"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)
            
        """if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            data = "22"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)"""
            #test om man bare kan holde en knap nede og den sender det samme tal hele tiden
        if event.type == pygame.key.get_pressed() and event.key == pygame.K_e:
            data = "22"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            data = "23"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)
            skt.sendto(nyt_data, (host, port))
            print(data)
            
        if event.type == pygame.K_q and event.key == pygame.K_t:
            data = "24"
            nyt_data = data.encode("UTF-8")
            skt.sendall(nyt_data)
          
    pygame.display.flip()
skt.close()