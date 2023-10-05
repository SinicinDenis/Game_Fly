import pygame
import random
import os


pygame.init()
screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[pygame.display.get_active()])
sc_xy = pygame.display.get_desktop_sizes()[pygame.display.get_active()]
clock = pygame.time.Clock()
FPS = 60
sp = []
riskanie = []
i = 0
fl = False
alpha = 255
zagruzka = pygame.image.load('shester.png').convert_alpha()
zagruzka = pygame.transform.scale(zagruzka, (500,500))
zagruzka1 = pygame.transform.rotate(zagruzka, 15)
ob_za = pygame.image.load('zu.png').convert_alpha()

zzz = 0

pygame.mouse.set_visible(False)
pos = pygame.mouse.get_pos()

def zagruzka_vsego():
    img_z = pygame.transform.rotate(zagruzka, zzz)
    img_l = pygame.transform.rotate(zagruzka1, -zzz)

    screen.blit(img_z, (sc_xy[0] // 3 - img_z.get_width() // 2 - 6, sc_xy[1] // 2 - img_z.get_height() // 2))
    screen.blit(img_l,
                ((sc_xy[0] - sc_xy[0] // 3) - img_l.get_width() // 2 + 6, sc_xy[1] // 2 - img_l.get_height() // 2))
    screen.blit(ob_za, (sc_xy[0] // 2 - ob_za.get_width() // 2, sc_xy[1] - sc_xy[1] // 5 - ob_za.get_height() // 2))
    pygame.display.update()

while True:
    screen.fill((0, 0, 0))
    if not sp:
        for ii in os.listdir('oboi\\'):
            zzz += 3
            screen.fill((0, 0, 0, 0))
            sp += [pygame.image.load('oboi\\'+ii).convert()]
            zagruzka_vsego()

        img = random.choice(sp)
        y = img.get_height() / sc_xy[0]
        for ii in os.listdir('player\\riskanie'):
            zzz += 3
            screen.fill((0, 0, 0, 0))
            riskanie += [pygame.image.load('player\\riskanie\\'+ii).convert()]
            zagruzka_vsego()

    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pos = (pos[0],pos[1]+10)

    if i < 255:
        im = img.subsurface(i+pos[0],pos[1]*int(y),*sc_xy)
        im.set_alpha(i)
        screen.blit(im, (0,0))
    elif i > 255 and not fl:
        screen.blit(img.subsurface(i + pos[0], pos[1]*int(y), *sc_xy), (0, 0))
        if i == img.get_width()- sc_xy[0]*2-256:
            fl = True
    elif fl:
        im = img.subsurface(i + pos[0], pos[1]*int(y), *sc_xy)
        im.set_alpha(alpha)
        screen.blit(im, (0, 0))
        alpha -= 1
        if alpha < 0:
            img = random.choice(sp)
            alpha = 255
            i = 0
            fl = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()