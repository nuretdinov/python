# pip install pygame
import pygame
import random

pygame.init()
gamewindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Older Superman in a galaxy far, far away")
pygame.key.set_repeat(2, 15) # повторение нажатия клавиш
clock = pygame.time.Clock()

running = True

# размещаем героя
hero_x = 250
hero_y = 280
hero_look = True # для отражения при движении вправо/влево героя
hero_sprite = pygame.image.load("static/img/hero.png")
hero_sprite = pygame.transform.scale(hero_sprite, (100,100))
gamewindow.blit(hero_sprite, (hero_x, hero_y))

# размещаем мобов
alien_x = 750
alien_y = random.randrange(100,500)
alien_sprite = pygame.image.load("static/img/alien.png")
gamewindow.blit(alien_sprite, (alien_x, alien_y))
alien_rect = alien_sprite.get_rect()

# фон
background = pygame.image.load("static/img/bg.jpg").convert()
background_rect = background.get_rect()

while running:

    clock.tick(24)

    #перемещение моба
    alien_x += random.randrange(-30, 0)
    alien_y += random.randrange(-20, 20)
    if alien_x < 0:
        alien_x = 750
        alien_y = random.randrange(100, 500)
    #контролируем, чтобы не вышел за экран
    if alien_y < 10:
        alien_y += 20
    if alien_y > 590:
        alien_y -= 20


    for event in pygame.event.get():
        # движение героя
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if hero_look:
                    hero_sprite = pygame.transform.flip(hero_sprite, True, False)
                    hero_look = False
                if hero_x > 5:
                    hero_x -= 10
            elif event.key == pygame.K_RIGHT:
                if not hero_look:
                    hero_sprite = pygame.transform.flip(hero_sprite, True, False)
                    hero_look = True
                if hero_x < 700:
                    hero_x += 10
            elif event.key == pygame.K_UP:
                if hero_y > 5:
                    hero_y -= 10
            elif event.key == pygame.K_DOWN:
                if hero_y < 500:
                    hero_y += 10


    gamewindow.blit(hero_sprite, (hero_x, hero_y))
    gamewindow.blit(alien_sprite, (alien_x, alien_y))
    pygame.display.update()
    gamewindow.fill((0, 0, 0)) # очистка экрана
    gamewindow.blit(background, background_rect)


    # корректный выход
    if event.type == pygame.QUIT:
        running = False

pygame.quit()