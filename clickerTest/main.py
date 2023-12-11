import pygame
from tkinter import messagebox

W = 640
H = 480
FPS = 30
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Test click speed")
clock = pygame.time.Clock()
# храним количество кликов
clicks_num = 0

running = True
# переменная для заставки и остановки по таймеру
start = False
# для времени, чтобы компенсировать паузу при заставке
pause = 0

while running:

    clock.tick(FPS)

    # время в секундах
    time = pygame.time.get_ticks() // 1000 - pause
    # для остановки на 30 сек
    if time >= 5:
        if start:
            messagebox.showinfo('Finished', f'You made {clicks_num} clicks')
            clicks_num = 0
            start = False

    if not start:
        # заставка
        start_text = pygame.font.Font(None, 40)
        start_text_render = start_text.render('- SPACE TO START CLICKS! -', True, (255, 255, 255))
        screen.blit(start_text_render, (130, 220))
        pygame.display.update()
    else:
        # выводим количество кликов когад играем
        score_font = pygame.font.Font(None, 522)
        score_text = score_font.render(str(clicks_num), True, (255, 255, 0))
        if clicks_num < 10:
            posX = W / 3
        elif 10 < clicks_num < 100:
            posX = W / 4 - 50
        else:
            posX = W / 5 - 120
        screen.blit(score_text, (posX, 70))
        # таймер
        clock_font = pygame.font.Font(None, 80)
        clock_text = clock_font.render(str(time), True, (255, 255, 255))
        screen.blit(clock_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # старт игры при заставке
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # запускаем игру
                    start = True
                    # устанавливаем значение паузы пока была заставка, чтобы таймер шел с нуля
                    pause = pygame.time.get_ticks() // 1000

            if start:
                # считаем клики, отслеживаем нажатие кнопок мыши (левой кнопки)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicks_num += 1

    pygame.display.update()
    screen.fill((0, 0, 0))


pygame.quit()
