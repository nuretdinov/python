import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Older Superman in a galaxy far, far away")
clock = pygame.time.Clock()

# добавляем музыку
pygame.mixer.music.load("static/music/music.mp3")
pygame.mixer.music.play()
blow_sound = pygame.mixer.Sound("static/music/blow_sound.mp3")

class Player(pygame.sprite.Sprite):
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


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("static/img/alien.png")
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
            alien_score +=1


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


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
def add_mobs(num):
    for i in range(num):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
add_mobs(10)
blows = pygame.sprite.Group()

# фон
background = pygame.image.load("static/img/bg.jpg").convert()
background_rect = background.get_rect()

running = True
hero_score = 0
alien_score = 0

while running:

    clock.tick(FPS)

    hits = pygame.sprite.spritecollide(player, mobs, True)
    for hit in hits:
        blow = Blow(hit.rect.center)
        all_sprites.add(blow)
        blows.add(blow)
        blow_sound.play()
        add_mobs(3)
        hero_score += 1

    screen.blit(background, background_rect)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()

    # не выводится !
    score_title_font = pygame.font.Font(None, 32)
    score_font = pygame.font.Font(None, 28)
    score_title = score_title_font.render('Score', True, (180, 180, 0))
    hero_score_text = score_font.render(f'Hero: {hero_score}', True, (180, 180, 0))
    alien_score_text = score_font.render(f'Alien: {alien_score}', True, (180, 180, 0))
    screen.blit(score_title, (20, 510))
    screen.blit(hero_score_text, (20, 540))
    screen.blit(alien_score_text, (20, 560))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
