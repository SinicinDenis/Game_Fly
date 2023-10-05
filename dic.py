import pygame
import os
# Инициализация Pygame
pygame.init()
d_cifri = {}


for ii in os.listdir('cifri\\'):
    d_cifri[ii] = []
    for jj in os.listdir(f'cifri\\{ii}\\'):
        d_cifri[ii] += [pygame.image.load(f'cifri\\{ii}\\{jj}').convert_alpha()]
    #d_cifri[ii] = [pygame.image.load('cifri\\' + ii +'\\' + jj).convert() for jj in os.listdir('cifri\\' + ii + '\\')]

print(d_cifri.keys())