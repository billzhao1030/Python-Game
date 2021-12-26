import pygame
from plane_sprites import *

pygame.init()  # Game initiation

# Set screen to 480 * 700
screen = pygame.display.set_mode((480, 700))


# Load the pictures
background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")

screen.blit(background, (0, 0))  # Top-left
screen.blit(hero, (150, 300))

# After draw everything update the screen
pygame.display.update()

# Clock object
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)  # position of hero

# sprites group
enemy = GameSprite("./images/enemy1.png")
enemy_group = pygame.sprite.Group(enemy)

while True:
    # set rate 60
    clock.tick(60)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit...")

            pygame.quit()
            exit()

    # update hero position
    hero_rect.y -= 1

    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700

    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    # sprites update and draw
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
