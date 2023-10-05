import pygame
import os
import sys
import random


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.vv = -1
        self.vn = -1
        self.i = -1
        self.j = 1

    def update(self):
        #self.j += 1
        if povorot[1] < 0:
            self.i = 0
            if self.vn > 0:
                self.vn -= 1
                screen.blit(vniz[self.vn % len(vniz)],
                            (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
            else:
                self.vv += 1
                if self.vv >= len(vverh)-1:
                    self.vv = len(vverh)-1
                    self.j += 1
                    if self.j % 15 == 0:
                        povorot_sound.play()
                    screen.blit(vverh[-1],
                                (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
                else:
                    screen.blit(vverh[self.vv % len(vverh)],
                                (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
        elif povorot[1] > 0:
            self.i = 0
            if self.vv > 0:
                self.vv -= 1
                screen.blit(vverh[self.vv % len(vverh)],
                            (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
            else:
                if self.vn >= len(vniz)-1:
                    self.vn = len(vniz)
                    self.j += 1
                    if self.j % 15 == 0:
                        povorot_sound_invert.play()
                    screen.blit(vniz[-1],
                                (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
                else:
                    self.vn += 1
                    screen.blit(vniz[self.vn % len(vniz)],
                                (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
        else:
            if self.vn > 0:
                self.vn -= 1
                screen.blit(vniz[self.vn%len(vniz)],
                            (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
                if self.vn == 0:
                    self.i = 0

            elif self.vv > 0:
                self.vv -= 1
                screen.blit(vverh[self.vv%len(vverh)],
                            (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))
                if self.vv == 0:
                    self.i = 0
            else:
                if self.vv < 1 and self.vn < 1:
                    self.i+=1
                    screen.blit(bochka[self.i % len(bochka)],
                                (pygame.mouse.get_pos()[0] - 200, pygame.mouse.get_pos()[1] - 177))





pygame.init()
if pygame.display.get_active():
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[pygame.display.get_active()], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[pygame.display.get_active()]
else:
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[-1], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[-1]

clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.set_num_channels(128)
pygame.mouse.set_visible(False)

FPS = 30

bochka = [pygame.image.load('player/bochka/' + ii).convert_alpha() for ii in os.listdir('player/bochka')]
vverh = [pygame.image.load('player/vverh/' + ii).convert_alpha() for ii in os.listdir('player/vverh')]
vniz = [pygame.image.load('player/vniz/' + ii).convert_alpha() for ii in os.listdir('player/vniz')]

povorot = pygame.mouse.get_rel()
sprites = pygame.sprite.Group()
sprites.add(Player())
pygame.mixer.music.load('player/player_sound.mp3')
povorot_sound = pygame.mixer.Sound('player/povorot_sound.mp3')
povorot_sound_invert = pygame.mixer.Sound('player/povorot_sound_invert.mp3')

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
while True:

    screen.fill((0, 0, 0))
    povorot = pygame.mouse.get_rel()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    sprites.update()

    pygame.display.flip()
    clock.tick(FPS)
