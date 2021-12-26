import pygame

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

hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    # set rate 60
    clock.tick(60)

    hero_rect.y -= 1

    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700

    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()

    pass

pygame.quit()  # Game quit
