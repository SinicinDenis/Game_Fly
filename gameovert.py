import pygame
import os
import sys
import random
import pygame.camera


def game_over():
    wall_group = pygame.sprite.Group()
    text_group = pygame.sprite.Group()
    text_group.add(Anim_texe())
    pygame.display.update()
    clock.tick(FPS)
    pygame.time.set_timer(pygame.USEREVENT + 2, random.randint(500, 5000))
    pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(5000, 13000))
    while True:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #elif event.type == pygame.USEREVENT + 1:
            #    wall_group.add(Karkozabric())
            #    pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(2000, 3000))
            elif event.type == pygame.USEREVENT + 2:
                wall_group.add(*[Listya() for i in range(200)])
                pygame.time.set_timer(pygame.USEREVENT + 2, random.randint(500, 5000))
        wall_group.update()
        text_group.update()
        pygame.display.update()
        print(len(wall_group))
        clock.tick(FPS)


class Anim_texe(pygame.sprite.Sprite):
    def __init__(self):
        super(Anim_texe, self).__init__()
        self.gameover_anim = gameover_anim
        self.i = 0

    def update(self):
        self.i += 1
        screen.blit(self.gameover_anim[self.i%len(self.gameover_anim)], (100,200))


class Listya(pygame.sprite.Sprite):
    def __init__(self):
        super(Listya, self).__init__()
        self.img = random.choice(listiki)
        self.x = random.randint(sc_xy[0], sc_xy[0] + 1500)
        self.y = random.randint(50, sc_xy[1]-50)
        self.engel = 0
        self.rect = pygame.Rect(self.x, self.y,50,50)
        self.i = random.randint(-5, 5)

    def update(self):
        self.engel += self.i
        self.rect.move_ip(-7-self.i, random.randint(-1, 1)+self.i)
        screen.blit(pygame.transform.rotate(self.img, self.engel), self.rect)
        if self.rect.right < -50 or self.rect.top < -50 or self.rect.bottom > 1330:
            self.kill()



pygame.init()

if pygame.display.get_active():
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[pygame.display.get_active()], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[pygame.display.get_active()]
else:
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[-1], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[-1]

listiki = []
gameover_anim = []

for ii in os.listdir('listiki/'):
    screen.fill((0,0,0))
    img_list = pygame.image.load('listiki/' + ii).convert_alpha()
    listiki += [pygame.transform.scale(img_list, (50, 50))]

for ii in os.listdir('gamover_anim/'):
    screen.fill((0,0,0))
    img_text = pygame.image.load('gamover_anim/' + ii).convert_alpha()
    gameover_anim += [pygame.transform.scale(img_text, (800,1000))]



clock = pygame.time.Clock()
FPS = 60

game_over()
