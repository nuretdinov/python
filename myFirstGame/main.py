# pip install pygame
import pygame
import random

pygame.init()
gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Older Superman in a galaxy far, far away")
pygame.key.set_repeat(2, 15) # повторение нажатия клавиш
clock = pygame.time.Clock()
background = pygame.image.load("static/img/bg.jpg").convert() # фон
background_rect = background.get_rect()
blow_sprite = pygame.image.load("static/img/blow.png") # взрыв
blow_rect = background.get_rect()

alien_score=0
hero_score=0

# размещаем героя
hero_x = 150
hero_y = 250
hero_look = True # для отражения при движении вправо/влево героя
hero_sprite = pygame.image.load("static/img/hero.png")
hero_rect = hero_sprite.get_rect()

# размещаем моба
alien_x = 750
alien_y = random.randrange(100, 500)
alien_sprite = pygame.image.load("static/img/alien.png")
alien_rect = alien_sprite.get_rect()


running = True

while running:

    clock.tick(24) #fps

    #перемещение моба
    rand_x = random.randrange(-30, 0)
    rand_y = random.randrange(-20, 20)
    alien_x += rand_x
    alien_rect.centerx = alien_x
    alien_y += rand_y
    alien_rect.centery = alien_y
    if alien_x < 0:
        alien_score += 1
        alien_x = 750
        alien_rect.centerx = alien_x
        alien_y = random.randrange(100, 500)
        alien_rect.centery = alien_y

    for event in pygame.event.get():
        # движение героя
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if hero_look:
                    hero_sprite = pygame.transform.flip(hero_sprite, True, False)
                    hero_look = False
                if hero_x > 5:
                    hero_x -= 10
                    hero_rect.centerx = hero_x
            elif event.key == pygame.K_RIGHT:
                if not hero_look:
                    hero_sprite = pygame.transform.flip(hero_sprite, True, False)
                    hero_look = True
                if hero_x < 690:
                    hero_x += 10
                    hero_rect.centerx = hero_x
            elif event.key == pygame.K_UP:
                if hero_y > 5:
                    hero_y -= 10
                    hero_rect.centery = hero_y
            elif event.key == pygame.K_DOWN:
                if hero_y < 500:
                    hero_y += 10
                    hero_rect.centery = hero_y


    gamewindow.blit(hero_sprite, (hero_x, hero_y))
    gamewindow.blit(alien_sprite, (alien_x, alien_y))

    if pygame.Rect.colliderect(alien_rect, hero_rect):
        collide = True
        gamewindow.blit(blow_sprite, (alien_x, alien_y))
        alien_x = 750
        alien_rect.centerx = alien_x
        alien_y = random.randrange(100, 500)
        alien_rect.centery = alien_y
        hero_score += 1
    else:
        collide = False

    pygame.display.update()
    gamewindow.blit(background, background_rect)

    f1 = pygame.font.Font(None, 28)
    text1 = f1.render(f'Hero: {hero_score}', True, (180, 180, 0))
    text2 = f1.render(f'Alien: {alien_score}', True, (180, 180, 0))
    gamewindow.blit(text1, (20, 540))
    gamewindow.blit(text2, (20, 560))

    # корректный выход
    if event.type == pygame.QUIT:
        running = False


pygame.quit()