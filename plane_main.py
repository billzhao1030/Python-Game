import pygame
from plane_sprites import *


class PlaneGame:

    def __init__(self):
        # create window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create clock
        self.clock = pygame.time.Clock()
        # create sprite
        self.__create_sprite()

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprite(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        while True:
            # set rate
            self.clock.tick(FRAME_PER_SECOND)

            # event handler
            self.__event_handler()

            # collision detection
            self.__check_collide()

            # update sprite
            self.__update_sprites()

            # update screen
            pygame.display.update()


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        pass

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    # create game object
    game = PlaneGame()

    game.start_game()
