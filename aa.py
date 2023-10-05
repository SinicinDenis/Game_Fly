import sys

import pygame
import random
import os


pygame.init()
if pygame.display.get_active():
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[pygame.display.get_active()], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[pygame.display.get_active()]
else:
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[-1], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[-1]

clock = pygame.time.Clock()
FPS = 30
oboi = []
dron = []
oboi_z = []

#for i in os.listdir('kosmolet\\'):
#    img_n = pygame.transform.scale(pygame.image.load('kosmolet\\' + i), sc_xy).convert_alpha()
#    oboi += [img_n]
#for i in os.listdir('DRON\\'):
#    img_n = pygame.transform.scale(pygame.image.load('DRON\\' + i), sc_xy).convert_alpha()
#    dron += [img_n]
for i in os.listdir('OBOI_ZASTAVKA\\'):
    img_n = pygame.transform.scale(pygame.image.load('OBOI_ZASTAVKA\\' + i), sc_xy).convert_alpha()
    oboi_z += [img_n]


i = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    i += 1
    if i == len(oboi_z):
        i = 0
    screen.blit(oboi_z[i], (0, 0))
    clock.tick(FPS)
    pygame.display.flip()

