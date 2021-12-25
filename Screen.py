import pygame

pygame.init()

# Set screen to 480 * 700
screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")

screen.blit(background, (0, 0))  # Top-left

pygame.display.update()

while True:
    pass

pygame.quit()
