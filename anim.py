import os, pygame, sys

pygame.init()

size = width, height = 800, 800
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
anim = [pygame.image.load('animation_boby\\fly_1\\' + ii).convert_alpha() for ii in
        os.listdir('animation_boby\\fly_1\\')]
i = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    i += 1
    screen.fill(black)
    screen.blit(anim[i % len(anim)], (0, 0))
    pygame.display.flip()
    clock.tick(60)