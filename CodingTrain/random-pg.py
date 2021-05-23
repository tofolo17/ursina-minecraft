from random import randint

import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Random')

position_x = 0
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    position_x = randint(0, 640)

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [position_x, 230, 20, 20])

    pygame.display.flip()
