import sys
from threading import Thread
import pygame
import random
import os


class Cifri:
    ochki = 0

    def __init__(self):
        self.i = -1

    def draw(self):
        self.i += 1
        self.nomer = 1
        for cc in str(Cifri.ochki):
            screen.blit(d_cifri[cc][self.i % len(d_cifri[cc])], (self.nomer*65, 50))
            self.nomer += 1


class Player:
    zdorov = 100

    def __init__(self):
        self.i = -1

    def draw(self):
        self.i += 1
        if self.i == len(bochka):
            self.i = 0
        screen.blit(bochka[self.i], (pygame.mouse.get_pos()[0]-200, pygame.mouse.get_pos()[1]-200))
        if Player.zdorov < 1:
            self.game_over()
        if Player.zdorov > -1 and Player.zdorov < 101:
            screen.blit(zdorov_p[Player.zdorov], (50, sc_xy[1]-100))
        if Weapon.n == 1:
            screen.blit(raketa, (410, sc_xy[1]-85))
        elif Weapon.n == 2:
            screen.blit(raketa, (410, sc_xy[1] - 105))
            screen.blit(raketa, (410, sc_xy[1] - 85))
            screen.blit(raketa, (410, sc_xy[1] - 65))

    def game_over(self):
        wall_group=pygame.sprite.Group()
        text_group=pygame.sprite.Group()
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
                # elif event.type == pygame.USEREVENT + 1:
                #    wall_group.add(Karkozabric())
                #    pygame.time.set_timer(pygame.USEREVENT + 1, random.randint(2000, 3000))
                elif event.type == pygame.USEREVENT + 2:
                    wall_group.add(*[Listya() for i in range(200)])
                    pygame.time.set_timer(pygame.USEREVENT + 2, random.randint(500, 5000))
            wall_group.update()
            text_group.update()
            pygame.display.update()
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

class Weapon:
    n = 1

    def __init__(self, st='0'):
        self.n = Weapon.n
        self.i = 1
        self.x = 0
        self.pos = pygame.mouse.get_pos()
        self.pos_weapon = 0
        self.st = st
        if self.n == 1:
            zapusk_raket.play()
        elif self.n == 2:
            troinoy.play()

    def draw(self):
        self.x += 1
        self.i += self.x
        if self.st == '0':
            self.pos_weapon = pygame.Rect(self.pos[0]+self.i-40, self.pos[1]-20, 80, 40)
            screen.blit(raketa, (self.pos[0]+self.i-40, self.pos[1]-20))
        elif self.st == '-':
            self.pos_weapon = pygame.Rect(self.pos[0] + self.i - 40, self.pos[1]-self.x*2 - 20, 80, 40)
            screen.blit(raketa, (self.pos[0] + self.i - 40, self.pos[1]-self.x*2 - 20))
        elif self.st == '+':
            self.pos_weapon = pygame.Rect(self.pos[0] + self.i - 40, self.pos[1] + self.x * 2 - 20, 80, 40)
            screen.blit(raketa, (self.pos[0] + self.i - 40, self.pos[1] + self.x * 2 - 20))
        if self.i > 1200:
            prorisovka.remove(self)

    def col(self):
        return self.pos_weapon


class Enemy:
    zdorov = 100

    def __init__(self, pos_enemy):
        self.x = 0
        self.y = pos_enemy
        self.i = -1
        self.pos = (sc_xy[0]-self.x, self.y, 128, 100)

    def draw(self):
        self.x += 3
        self.i += 1
        if self.i == len(enemy):
            self.i = 0
        self.pos = pygame.Rect(sc_xy[0]-self.x, self.y, 128, 100)
        screen.blit(enemy[self.i], (sc_xy[0]-self.x, self.y))
        if self.x > 1200 and self in prorisovka:
            prorisovka.remove(self)

    def col(self):
        return self.pos

    def col_vzriv(self):
        return sc_xy[0] - self.x, self.y - 70


class VistrelEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.i = 0
        self.ii = 1

    def draw(self):
        self.ii += 1
        self.i += self.ii
        screen.blit(pulya_enemy, (self.x - self.i, self.y+100))
        if self.x - self.i < -50:
            prorisovka.remove(self)

    def pos(self):
        return pygame.Rect(self.x - self.i, self.y+100, pulya_enemy.get_width(),pulya_enemy.get_height()), (self.x - self.i-200, self.y+100)


class Vzriv:
    def __init__(self, enemy_pos_v):
        self.enemy_pos_v = enemy_pos_v
        self.i=-1
        self.vzr = random.choice(list(EXPLOITED_enemy.values()))

    def draw(self):
        self.i+=1
        if self.i == len(self.vzr):
            prorisovka.remove(self)
            return
        screen.blit(self.vzr[self.i], (self.enemy_pos_v))


class MalVzriv:
    def __init__(self,p_pos):
        self.i = -1
        self.p_pos = p_pos
        kevlar4.play()
        self.rand_exploited = random.choice(list(d_exploited.keys()))

    def draw(self):
        self.i += 1
        if self.i == len(d_exploited[self.rand_exploited]):
            prorisovka.remove(self)
            return
        screen.blit(d_exploited[self.rand_exploited][self.i], self.p_pos)


class Menu:
    def __init__(self):
        self.i = -1

    def draw(self):
        self.i += 1
        if self.i == len(menu):
            self.i = 0

        screen.blit(menu[self.i], (0, 0))


class Button:
    def __init__(self, x, y, width, height, sp_n, sp_0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.i = -1
        self.sp_n = sp_n
        self.sp_0 = sp_0
        self.fl = False

    def draw(self):
        self.i += 1
        if self.i == len(self.sp_n):
            self.i = 0
        if self.fl:
            screen.blit(self.sp_n[self.i], (self.x, self.y))
        else:
            screen.blit(self.sp_0[self.i], (self.x, self.y))


class Cursor:
    def __init__(self):
        self.i = -1

    def draw(self):
        self.i += 1
        screen.blit(MENU_dic['cursor'][self.i % len(MENU_dic['cursor'])], pygame.mouse.get_pos())


class Karkozabric:
    def __init__(self, n=0):
        self.n = n
        self.i = 256
        self.x = sc_xy[0] + random.randint(0, 10)
        self.y = random.randint(1, sc_xy[1])
        self.sc = random.randint(3, 26)
        self.alpha = random.randint(1, 5)
        self.rect = None

    def draw(self):
        if self.i < 5:
            if self in menu_prorisovka:
                menu_prorisovka.remove(self)
        else:
            self.i -= self.alpha
            self.x -= random.randint(1, 10)
            self.y += random.randint(-5, 5)
            self.rect = pygame.Surface((self.sc, self.sc), pygame.SRCALPHA)
            if self.n == 1:
                self.rect.fill((random.randint(50, 155), random.randint(0, 55), 0, self.i))
            elif self.n == 2:
                self.rect.fill((random.randint(0, 55), 55, random.randint(0, 55), self.i))
            elif self.n == 4:
                self.rect.fill((random.randint(0, 100), 0, random.randint(0, 100), self.i))
            elif self.n == 3:
                self.rect.fill((50, 50, random.randint(0, 165), self.i))
            elif self.n == 0:
                self.rect.fill((random.randint(0, 90), random.randint(0, 30), random.randint(0, 30), self.i))
            screen.blit(self.rect, (self.x, self.y))


class Treshina_na:
    def __init__(self):
        self.i = 256
        self.x = random.randint(0,sc_xy[0])
        self.y = random.randint(0,sc_xy[1])
        self.angle = random.randint(1, 360)
        self.scale = random.uniform(0.1, 0.3)
        self.img = pygame.transform.rotozoom(treshina, self.angle, self.scale)

    def draw(self):
        self.i -= 1
        if self.i < 1:
            prorisovka.remove(self)
            return
        self.img.set_alpha(self.i)
        screen.blit(self.img, (self.x, self.y))


def zagruzka_vsego():
    me.draw()
    img_z = pygame.transform.rotate(zagruzka, zzz)
    img_l = pygame.transform.rotate(zagruzka1, -zzz)

    screen.blit(img_z, (sc_xy[0] // 3 - img_z.get_width() // 2 - 6, sc_xy[1] // 2 - img_z.get_height() // 2))
    screen.blit(img_l,
                ((sc_xy[0] - sc_xy[0] // 3) - img_l.get_width() // 2 + 6, sc_xy[1] // 2 - img_l.get_height() // 2))
    screen.blit(ob_za, (sc_xy[0] // 2 - ob_za.get_width() // 2, sc_xy[1] - sc_xy[1] // 5 - ob_za.get_height() // 2))
    pygame.display.update()


def menu_():
    global menu_prorisovka
    menu_while = True
    new_1=Button(50, 50, 700, 200, MENU_dic['new_game'], MENU_dic['new_game_0'])
    new_2=Button(50, 250, 700, 200, MENU_dic['zagr_im'], MENU_dic['zagr_im_0'])
    new_4=Button(50, 450, 700, 200, MENU_dic['nastroika'], MENU_dic['nastroika_0'])
    new_3=Button(50, 800, 700, 200, MENU_dic['vihod'], MENU_dic['vihod_0'])

    while menu_while:
        print(len(menu_prorisovka))
        screen.fill((0, 0, 0))
        for prorisovk in menu_prorisovka:
            prorisovk.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_while = False
            if new_1.rect.collidepoint(pygame.mouse.get_pos()):
                menu_prorisovka += [Karkozabric(1) for i in range(15)]
                if not new_1.fl:
                    random.choice(piano_c0).play()
                new_1.fl = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    menu_while = False
            else:
                new_1.fl = False
            if new_2.rect.collidepoint(pygame.mouse.get_pos()):
                menu_prorisovka += [Karkozabric(2) for i in range(5)]
                if not new_2.fl:
                    random.choice(piano_c0).play()
                new_2.fl = True
            else:
                new_2.fl = False
            if new_3.rect.collidepoint(pygame.mouse.get_pos()):
                menu_prorisovka += [Karkozabric(3) for i in range(5)]
                if not new_3.fl:
                    random.choice(piano_c0).play()
                new_3.fl = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.quit()
                    sys.exit()
            else:
                new_3.fl = False
            if new_4.rect.collidepoint(pygame.mouse.get_pos()):
                menu_prorisovka += [Karkozabric(4) for i in range(5)]
                if not new_4.fl:
                    random.choice(piano_c0).play()
                new_4.fl = True
            else:
                new_4.fl = False
        menu_prorisovka += [Karkozabric(0) for i in range(3)]
        new_1.draw()
        new_2.draw()
        new_3.draw()
        new_4.draw()
        curs.draw()
        pygame.display.update()
        clock.tick(FPS)


def IGRA_CIKL():
    global enemy_sp, prorisovka, weapon_sp, enemy_pulya_sp, img, y
    FPS=60
    i=0
    fl=False
    alpha=255
    igraTru=True
    while igraTru:
        screen.fill((0, 0, 0))
        i += 1
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 2:
                pygame.time.set_timer(pygame.USEREVENT + 2, random.randint(500, 3000))
                bullet_time.play()
                for eee in enemy_sp:
                    if sum(list(map(lambda x: type(x).__name__ == 'VistrelEnemy', prorisovka))) < 10:
                        prorisovka+=[VistrelEnemy(*eee.col_vzriv())]
            weapon_sp.clear()
            enemy_sp.clear()
            enemy_pulya_sp.clear()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Weapon.n=1
                elif event.key == pygame.K_2:
                    Weapon.n=2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Weapon.n == 1:
                    prorisovka.insert(0, Weapon())
                elif Weapon.n == 2:
                    prorisovka.insert(0, Weapon('-'))
                    prorisovka.insert(0, Weapon('+'))
                    prorisovka.insert(0, Weapon())

            if event.type == pygame.USEREVENT + 1:
                pos_enemy=random.randint(50, sc_xy[1])
                prorisovka+=[Enemy(pos_enemy)]

        if i < 255:
            if pos[1] < 647:
                im = img.subsurface(i + pos[0], int(pos[1] * y), *sc_xy)
                im.set_alpha(i)
                screen.blit(im, (0, 0))
            else:
                im=img.subsurface(i + pos[0], int(646 * y), *sc_xy)
                im.set_alpha(i)
                screen.blit(im, (0, 0))
        elif i > 255 and not fl:
            if pos[1] < 647:
                screen.blit(img.subsurface(i + pos[0], int(pos[1] * y), *sc_xy), (0, 0))
                if i == img.get_width() - sc_xy[0] * 2 - 256:
                    fl=True
            else:
                screen.blit(img.subsurface(i + pos[0], int(646 * y), *sc_xy), (0, 0))
                if i == img.get_width() - sc_xy[0] * 2 - 256:
                    fl=True
        elif fl:
            if pos[1] < 647:
                im=img.subsurface(i + pos[0], int(pos[1] * y), *sc_xy)
            else:
                im=img.subsurface(i + pos[0], int(646 * y), *sc_xy)
            im.set_alpha(alpha)
            screen.blit(im, (0, 0))
            alpha-=1
            if alpha < 0:
                img=random.choice(sp)
                y=img.get_height() / sc_xy[1]
                alpha=255
                i=0
                fl=False

        for ii in prorisovka:
            if type(ii).__name__ == 'Weapon':
                weapon_sp+=[ii]
            elif type(ii).__name__ == 'Enemy':
                enemy_sp+=[ii]
            elif type(ii).__name__ == 'VistrelEnemy':
                enemy_pulya_sp+=[ii]
            ii.draw()
        flag=False

        for ii in enemy_pulya_sp:
            if ii.pos()[0].colliderect(pygame.mouse.get_pos()[0] + 190, pygame.mouse.get_pos()[1] - 200, 10, 400):
                prorisovka+=[MalVzriv(ii.pos()[1])]
                if sum(list(map(lambda x: type(x).__name__ == 'Treshina_na', prorisovka))) < 10:
                    prorisovka+=[Treshina_na()]
                prorisovka.remove(ii)
                enemy_pulya_sp.clear()
                Player.zdorov-=5

        for ii in weapon_sp:
            if flag:
                break
            for jj in enemy_sp:
                if ii.col().colliderect(jj.col()):
                    if len(prorisovka) == 0:
                        break
                    if ii in prorisovka:
                        prorisovka.remove(ii)
                    if jj in prorisovka:
                        prorisovka.insert(0, Vzriv(jj.col_vzriv()))
                        prorisovka.remove(jj)
                        vzriv.play()
                        Cifri.ochki+=1
                    flag=True
                    break
        pygame.display.flip()
        clock.tick(FPS)


def work(x, di, ii):
    di[ii] += [pygame.image.load(x).convert_alpha()]


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

FPS = 60
sp = []
menu_nachalo = True
riskanie = []
bochka = []
enemy = []
prorisovka = []
menu = []
piano_c0 = []
vzriv_img = []
zdorov_p = []

weapon_sp = []
enemy_sp = []
enemy_pulya_sp = []

mal_vzriv = []
exp_3 = []
exp_4 = []

listiki = []
gameover_anim = []

i = 0
fl = False
alpha = 255

pulya_enemy = pygame.image.load('pulya_enemy.png').convert_alpha()
pulya_enemy = pygame.transform.rotozoom(pulya_enemy, -180, 0.05)
raketa = pygame.image.load('raketa.png').convert_alpha()
raketa = pygame.transform.rotozoom(raketa, -90, 0.05)
zagruzka = pygame.image.load('shester.png').convert_alpha()
zagruzka = pygame.transform.scale(zagruzka, (400, 400))
zagruzka1 = pygame.transform.rotate(zagruzka, 15)
ob_za = pygame.image.load('zu.png').convert_alpha()
treshina = pygame.image.load('treshina.png').convert_alpha()

zzz = 0


for ii in os.listdir('menu/'):
    menu += [pygame.transform.scale(pygame.image.load('menu/' + ii), sc_xy).convert_alpha()]

zdorov_p = [pygame.image.load('zdorov/' + ii).convert_alpha() for ii in sorted(os.listdir('zdorov/'))]

prorisovka += [Player()]

me = Menu()

pos = pygame.mouse.get_pos()

threads = []

d_cifri = {}

for ii in os.listdir('cifri/'):
    d_cifri[ii] = []
    for jj in os.listdir(f'cifri/{ii}/'):
        threads.append(Thread(target=work(f'cifri/{ii}/{jj}',d_cifri, ii)))

d_exploited = {}

for ii in os.listdir('PixelSimulations/'):
    d_exploited[ii] = []
    for jj in os.listdir(f'PixelSimulations/{ii}/'):
        threads.append(Thread(target=work(f'PixelSimulations/{ii}/{jj}',d_exploited, ii)))


EXPLOITED_enemy = {}

for ii in os.listdir('EXPLOITED_enemy/'):
    EXPLOITED_enemy[ii] = []
    for jj in os.listdir(f'EXPLOITED_enemy/{ii}/'):
        threads.append(Thread(target=work(f'EXPLOITED_enemy/{ii}/{jj}',EXPLOITED_enemy, ii)))

MENU_dic = {}

for ii in os.listdir('MENU_dic/'):
    MENU_dic[ii] = []
    for jj in os.listdir(f'MENU_dic/{ii}/'):
        threads.append(Thread(target=work(f'MENU_dic/{ii}/{jj}',MENU_dic, ii)))

for th in threads:
    th.start()

piano_c0 = [pygame.mixer.Sound('sounds/piano_c0/' + ii) for ii in os.listdir('sounds/piano_c0')]
zapusk_raket = pygame.mixer.Sound('sounds/weapon/zapusk_raket.mp3')
zapusk_raket.set_volume(0.3)
vzriv = pygame.mixer.Sound('sounds/weapon/vzriv.mp3')
vzriv.set_volume(0.2)
troinoy = pygame.mixer.Sound('sounds/weapon/troinoy.mp3')
troinoy.set_volume(0.1)
bullet_time = pygame.mixer.Sound('sounds/weapon/bullet-time.mp3')
bullet_time.set_volume(0.3)
kevlar4 = pygame.mixer.Sound('sounds/weapon/kevlar4.mp3')
kevlar4.set_volume(0.5)

curs = Cursor()
menu_prorisovka=[]

menu_()

sp = [pygame.image.load('oboi/' + ii).convert() for ii in os.listdir('oboi/')]
for ii in os.listdir('player/riskanie'):
    zzz += 1
    screen.fill((0, 0, 0, 0))
    riskanie += [pygame.image.load('player/riskanie/' + ii).convert()]
    zagruzka_vsego()
for ii in os.listdir('player/bochka'):
    zzz += 1
    screen.fill((0, 0, 0, 0))
    bochka += [pygame.image.load('player/bochka/' + ii).convert_alpha()]
    zagruzka_vsego()
for ii in os.listdir('enemy/'):
    zzz += 1
    screen.fill((0, 0, 0, 0))
    enemy += [pygame.image.load('enemy/' + ii).convert_alpha()]
    zagruzka_vsego()
for ii in os.listdir('vzriv/'):
    zzz += 1
    screen.fill((0, 0, 0, 0))
    vzriv_img += [pygame.image.load('vzriv/' + ii).convert_alpha()]
    zagruzka_vsego()
for ii in os.listdir('listiki/'):
    zzz += 1
    screen.fill((0,0,0))
    print('listiki/' + ii)
    img_list = pygame.image.load('listiki/' + ii).convert_alpha()
    listiki += [pygame.transform.scale(img_list, (75, 75))]
    zagruzka_vsego()
for ii in os.listdir('gamover_anim/'):
    screen.fill((0,0,0))
    img_text = pygame.image.load('gamover_anim/' + ii).convert_alpha()
    gameover_anim += [pygame.transform.scale(img_text, (400,200))]

img = random.choice(sp)
y = img.get_height() / sc_xy[1]

pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
pygame.time.set_timer(pygame.USEREVENT + 2, 2000)

prorisovka += [Cifri()]
IGRA_CIKL()
