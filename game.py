import pygame
import random
import sys
import pygame.gfxdraw


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (255, 0, 0), (50, 50), 35)
        self.x = sc_xy[0] // 2
        self.y = sc_xy[1] - 130
        self.speed = 5
        self.score = 0
        self.lives = 3
        self.level = 1

    def update(self):
        if pygame.mouse.get_pos()[0] < sc_xy[0] // 2:
            if self.x - self.speed > 0:
                self.x -= self.speed
        else:
            if self.x + self.speed < sc_xy[0]-100:
                self.x += self.speed
        screen.blit(self.image, (self.x, self.y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill((random.randint(100,255),random.randint(100,255),random.randint(100,255)))
        pygame.draw.circle(self.image, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), (50, 50), random.randint(10,55))
        self.x = random.randint(100, sc_xy[0]-100)
        self.y = 0
        self.speed = 5
        self.level = 1
        self.lives = 100
        self.f = pygame.font.SysFont(random.choice(pygame.font.get_fonts()[:10]), 36)
        self.text = self.f.render(f'{self.lives}', True, 'black')
        self.image.blit(self.text, (0, 50))
        self.otskok = True
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.image.get_rect()
        if self.x - self.speed > 0 and self.otskok:
            self.x -= self.speed
        else:
            self.otskok = False
        if self.x + self.speed < sc_xy[0]-100 and not self.otskok:
            self.x += self.speed
        else:
            self.otskok = True

        self.y += 1
        screen.blit(self.image, (self.x, self.y))

        if self.y > sc_xy[1]:
            self.kill()


class Pulya:
    pass

def game():
    clock = pygame.time.Clock()
    dt = 0
    i = 1
    bobo = True
    while True:
        if i == 255:
            bobo = False
        if i == 1:
            bobo = True
        if bobo:
            i += 1
        else:
            i -= 1
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == enemy_spawn:
                enemy = Enemy()
                sprite_enemy.add(enemy)
        #stolknoveniya_enemy = pygame.sprite.groupcollide(sprite_enemy, sprite_enemy, False, False)
        #for j in stolknoveniya_enemy:
        #    j.otskok = abs(j.otskok * 1 - 1)
        sprite_player.update()
        sprite_enemy.update()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


pygame.init()
if pygame.display.get_active():
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[pygame.display.get_active()], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[pygame.display.get_active()]
else:
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[-1], pygame.FULLSCREEN)
    sc_xy = pygame.display.get_desktop_sizes()[-1]

sprite_player = pygame.sprite.Group()
sprite_enemy = pygame.sprite.Group()
player = Player()
sprite_player.add(player)

enemy_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(enemy_spawn, 1000)
pulya_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(pulya_spawn, 100)

game()

