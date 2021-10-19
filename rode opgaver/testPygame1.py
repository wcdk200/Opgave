import pygame

def run_game():
    pygame.init()
    pygame.display.set_mode((320, 200))
    pygame.display.set_caption("Hello world")

    while True:
        for event in pygame.event.get():
            pygame.quit()
            exit()
        pygame.display.flip()

run_game()