from random import randint

import pygame
from perlin_noise import PerlinNoise

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Random')

noise = PerlinNoise(octaves=randint(1, 4), seed=randint(1, 9999))

i = 0
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    position_x = 190 + (noise(i) * 400)

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [position_x, 190, 20, 20])

    pygame.display.flip()

    i += 0.0001
