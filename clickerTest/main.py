import pygame
import time

W = 640
H = 480
FPS = 30
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Test click speed")
clock = pygame.time.Clock()
clicks_num = 0
running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicks_num += 1

    screen.fill((0,0,0))

    time = pygame.time.get_ticks()/1000
    clock_font = pygame.font.Font(None, 80)
    clock_text = clock_font.render(str(time), True, (255, 255, 255))
    screen.blit(clock_text, (10, 10))

    score_font = pygame.font.Font(None, 522)
    score_text = score_font.render(str(clicks_num), True, (255, 255, 0))
    if clicks_num < 10:
        posX = W/3
    elif 10 < clicks_num < 100:
        posX = W/4 - 50
    else:
        posX = W/5 - 120
    screen.blit(score_text, (posX, 70))

    pygame.display.update()

pygame.quit()
