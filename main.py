import pygame

BG_COLOR = (255, 127, 127)
W = 1440
H = 810
LEN = 40
FPS = 60

bg = pygame.image.load("Picture/zelda_bg.png")
bg2 = pygame.image.load("Picture/died_bg.png")
pygame.init()
music = pygame.mixer.Sound("Music/8-bit_music.mp3")
music.play()
music_died = pygame.mixer.Sound("Music/9c1cc8e40fe5836.mp3")
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Столкновение спрайтов")
pygame.display.flip()
clock = pygame.time.Clock()

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.image.load("Picture/Zelda.png").convert_alpha()
sprite1.rect = sprite1.image.get_rect(center=(600, 300))

sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.image.load("Picture/2dSprite.png").convert_alpha()
sprite2.rect = sprite2.image.get_rect(center=(720, 405))

all_sprites_group = pygame.sprite.Group([sprite1, sprite2])
game = True
dx1 = 0
dy1 = 0
dx2 = 0
dy2 = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx1 = -5
    if keys[pygame.K_RIGHT]:
        dx1 = 5
    if keys[pygame.K_UP]:
        dy1 = -5
    if keys[pygame.K_DOWN]:
        dy1 = 5
    sprite1.rect.x += dx1
    sprite1.rect.y += dy1
    dx1 = dy1 = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        dx2 = -5
    if keys[pygame.K_d]:
        dx2 = 5
    if keys[pygame.K_w]:
        dy2 = -5
    if keys[pygame.K_s]:
        dy2 = 5
    sprite2.rect.x += dx2
    sprite2.rect.y += dy2
    dx2 = dy2 = 0

    hit = pygame.sprite.collide_rect(sprite1, sprite2)

    if hit:
        bg_color = bg2
        screen.blit(bg_color, (0, 0))
        music_died.play()
    else:
        bg_color = bg
        screen.blit(bg_color, (0, 0))
    all_sprites_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
