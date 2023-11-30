# pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Older Superman in a galaxy far, far away")
pygame.key.set_repeat(2, 15)  # повторение нажатия клавиш
clock = pygame.time.Clock()
background = pygame.image.load("static/img/bg.jpg").convert()  # фон
background_rect = background.get_rect()
blow_sprite = pygame.image.load("static/img/blow.png")  # взрыв
blow_rect = background.get_rect()

# добавляем музыку
pygame.mixer.music.load("static/music/music.mp3")
pygame.mixer.music.play()
blow_sound = pygame.mixer.Sound("static/music/blow_sound.mp3")

alien_score = 0
hero_score = 0

# размещаем героя
hero_x = 150
hero_y = 250
hero_look = True  # для отражения при движении вправо/влево героя
hero_sprite = pygame.image.load("static/img/hero.png")
hero_rect = hero_sprite.get_rect()

# размещаем моба
alien_x = 750
alien_y = random.randrange(100, 500)
alien_sprite = pygame.image.load("static/img/alien.png")
alien_rect = alien_sprite.get_rect()

# заставка
start_screen = pygame.image.load("static/img/start.jpg").convert()
screen.blit(start_screen, (0, 0))
start_text = pygame.font.Font(None, 28)
start_text_render = start_text.render('[..... press space .....]', True, (180, 180, 0))
screen.blit(start_text_render, (300, 420))
pygame.display.update()

running = True
start = False

while running:

    # заставка ждет нажатия пробела
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    if start:
        clock.tick(24)  # fps

        # перемещение моба
        rand_x = random.randrange(-30, 0)
        rand_y = random.randrange(-20, 20)
        alien_x += rand_x
        alien_y += rand_y
        if alien_x < -30:
            alien_score += 1
            alien_x = 780
            alien_y = random.randrange(100, 500)
        if alien_y < 30:
            alien_y += 20
        if alien_y > 570:
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
                    if hero_x < 690:
                        hero_x += 10
                elif event.key == pygame.K_UP:
                    if hero_y > 5:
                        hero_y -= 10
                elif event.key == pygame.K_DOWN:
                    if hero_y < 500:
                        hero_y += 10

        screen.blit(hero_sprite, (hero_x, hero_y))
        hero_rect.centery = hero_y
        hero_rect.centerx = hero_x

        screen.blit(alien_sprite, (alien_x, alien_y))
        alien_rect.centerx = alien_x
        alien_rect.centery = alien_y

        if pygame.Rect.colliderect(alien_rect, hero_rect):
            screen.blit(blow_sprite, (alien_x, alien_y))
            alien_x = 750
            alien_rect.centerx = alien_x
            alien_y = random.randrange(100, 500)
            alien_rect.centery = alien_y
            hero_score += 1
            blow_sound.play()

        pygame.display.update()
        screen.blit(background, background_rect)

        score_font = pygame.font.Font(None, 22)
        score_text = score_font.render(f'[{hero_score}] hero VS alien [{alien_score}]', True, (180, 180, 0))
        screen.blit(score_text, (20, 560))

    # корректный выход
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
