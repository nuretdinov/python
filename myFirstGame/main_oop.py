import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Older Superman in a galaxy far, far away")
clock = pygame.time.Clock()
pygame.mixer.music.load("static/music/music.mp3")
pygame.mixer.music.play()
blow_sound = pygame.mixer.Sound("static/music/blow_sound.mp3")
background = pygame.image.load("static/img/bg.jpg").convert()
background_rect = background.get_rect()
alien_imgs = []
alien_list = ['static/img/alien.png', 'static/img/alien1.png', 'static/img/alien2.png', ]
for img in alien_list:
    alien_imgs.append(pygame.image.load(img))
# заставка
start_screen = pygame.image.load("static/img/start.jpg").convert()
screen.blit(start_screen, (0, 0))
start_text = pygame.font.Font(None, 24)
start_text_render = start_text.render('[..... press space .....]', True, (180, 180, 0))
screen.blit(start_text_render, (300, 420))
pygame.display.update()

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("static/img/hero.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(alien_imgs)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + self.rect.width
        self.rect.y = random.randrange(50, 550)
        self.speedy = random.randrange(1, 15)

    def update(self):
        global alien_score
        self.rect.x -= self.speedy
        self.rect.y += random.randrange(-10, 10)
        if self.rect.left < 0:
            self.rect.x = WIDTH + self.rect.width
            self.rect.y = random.randrange(50, 550)
            self.speedy = random.randrange(1, 10)
            alien_score += 1


class Blow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("static/img/blow.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.kill()


def add_aliens(num):
    for i in range(num):
        new_alien = Alien()
        all_sprites.add(new_alien)
        alians.add(new_alien)


all_sprites = pygame.sprite.Group()
hero = Hero()
all_sprites.add(hero)
alians = pygame.sprite.Group()
add_aliens(10)
blows = pygame.sprite.Group()

hero_score = 0
alien_score = 0
running = True
start = False

while running:

    # заставка ждет нажатия пробела
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    if start:

        clock.tick(FPS)

        hits = pygame.sprite.spritecollide(hero, alians, True)
        for hit in hits:
            blow = Blow(hit.rect.center)
            all_sprites.add(blow)
            blows.add(blow)
            blow_sound.play()
            add_aliens(3)
            hero_score += 1

        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)

        score_font = pygame.font.Font(None, 22)
        score_text = score_font.render(f'[{hero_score}] hero VS alien [{alien_score}]', True, (180, 180, 0))
        screen.blit(score_text, (20, 560))

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
