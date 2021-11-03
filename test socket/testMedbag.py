import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Motorstyring")


gameLoop = True

print("Kører klienten\n")

#winn = pygame.image.load("sjovTing.png")

while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            data = "17"
            nyt_data = data.encode("UTF-8")
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            data = "18"
            nyt_data = data.encode("UTF-8")
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            data = "22"
            nyt_data = data.encode("UTF-8")
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            data = "23"
            nyt_data = data.encode("UTF-8")
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            data = "24"
            nyt_data = data.encode("UTF-8")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:    
            data = "13"
            nyt_data = data.encode("UTF-8")     
          
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            data = "14"
            nyt_data = data.encode("UTF-8")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            data = "15"
            nyt_data = data.encode("UTF-8")

        #screen.blit(winn, [0, 0])

    pygame.display.flip()