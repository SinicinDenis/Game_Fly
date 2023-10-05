import pygame
import sys
import random

pygame.init()

WINDOW_SIZE = (400, 400)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

color1 = pygame.Color(0,0,0)
color2 = pygame.Color(255,255,255)
t = 0

fl = True

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    if t > 0.99:
        fl = False
        color1 = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    elif t < 0.01:
        fl = True
        color2 = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if fl:
        t = (t + 0.01) % 1
    else:
        t = (t - 0.01) % 1
    print(t)
    color = color1.lerp(color2, t)
    screen.fill(color)

    # Draw
    pygame.display.update()

    # Control FPS
    clock.tick(FPS)