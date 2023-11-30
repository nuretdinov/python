import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot em all! Yankee")
clock = pygame.time.Clock()
FPS = 50
pygame.mixer.music.load("static/music/music.mp3")
pygame.mixer.music.play()
shot_sound = pygame.mixer.Sound("static/music/shot.mp3")
show_sound = pygame.mixer.Sound("static/music/sound1.mp3")

nextbot_snds = []
nextbot_sound_list = ['static/music/sound1.mp3', 'static/music/sound2.mp3', 'static/music/sound3.mp3', ]
for snd in nextbot_sound_list:
    nextbot_snds.append(pygame.mixer.Sound(snd))

nextbot_imgs = []
nextbot_list = ['static/img/nextbot1.png', 'static/img/nextbot2.png', 'static/img/nextbot3.png', ]
for img in nextbot_list:
    nextbot_imgs.append(pygame.image.load(img))



class Nextbot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(nextbot_imgs)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 680)
        self.rect.y = random.randrange(50, 500)

class Shot(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("static/img/shot.png")
        self.rect = self.image.get_rect()
        self.rect.center = center

nextbot = Nextbot()
running = True
quantity = 0

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shot = Shot(event.pos)
                shot_sound.play()
                if pygame.Rect.colliderect(shot.rect, nextbot.rect):
                    print("!")
                    quantity = 0
                screen.blit(shot.image, shot.rect)
                print(event.pos)

    if pygame.time.get_ticks() > 5000 and pygame.time.get_ticks() % 10 == 0 and quantity == 0:
            nextbot = Nextbot()
            quantity = 1
            screen.blit(nextbot.image, nextbot.rect)
            random.choice(nextbot_snds).play()


    pygame.display.update()
    #screen.fill(BLACK)

pygame.quit()