import pygame
import pygame.camera
import random


class Karkozabric(pygame.sprite.Sprite):
    def __init__(self, n=0):
        super().__init__()
        self.image = pygame.transform.scale(cam.get_image(), (200, 200))
        self.rect = self.image.get_rect(center=(50,random.randint(1,1024)))
        self.n = n
        self.i = 1
        self.y = random.randint(1, window.get_height())
        self.sc = random.randint(3, 6)
        self.alpha = random.randint(1, 5)


    def update(self):
        self.i += 1
        #self.image = pygame.transform.scale(cam.get_image(), (i, i))

        if self.i > 500:
            self.kill()
        else:
            self.rect.x += 3



class Player(pygame.sprite.Sprite):
    def __init__(self, center_pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center = center_pos)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, center_pos):
        super().__init__()
        self.image = pygame.Surface((20, 10))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(center = center_pos)

    def update(self):
        self.rect.x += 10
        if self.rect.right > 300:
            self.kill()


pygame.init()
window = pygame.display.set_mode((1280, 1024), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(800,600))
cam.start()
pygame.time.set_timer(pygame.USEREVENT + 2, random.randint(500, 1000))


player = Player((25, window.get_height() // 2))
all_sprites = pygame.sprite.Group(player)

run = True
i = 1
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT + 2:
            all_sprites.add(Karkozabric())

    all_sprites.update()
    print(all_sprites)

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), (300, 0, 10, window.get_height()))
    all_sprites.draw(window)
    #img = pygame.transform.rotozoom(cam.get_image(),i, 1.5)
    #window.blit(img,(0,0))
    i += 10
    pygame.display.flip()

pygame.quit()
exit()