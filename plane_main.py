import pygame
from plane_sprites import *

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FPS = 60


class PlaneGame:

    def __init__(self):
        # create window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create clock
        self.clock = pygame.time.Clock()
        # create sprite
        self.__create_sprite()

    def __create_sprite(self):
        pass

    def start_game(self):
        while True:
            # set rate
            self.clock.tick(FPS)

            # event handler
            self.__event_handler()

            # collision detection
            self.__check_collide()

            # update sprite
            self.__update_sprites()

            # update screen
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    # create game object
    game = PlaneGame()

    game.start_game()
