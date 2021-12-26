import pygame

pygame.init()  # Game initiation

# Set screen to 480 * 700
screen = pygame.display.set_mode((480, 700))


# Load the pictures
background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")

screen.blit(background, (0, 0))  # Top-left
screen.blit(hero, (200, 500))

# After draw everything update the screen
pygame.display.update()

# Clock object
clock = pygame.time.Clock()



while True:

    clock.tick(60)
    pass

pygame.quit()  # Game quit
