import os
import pygame
from events import HandleEvents
from level import Level

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):

    def __init__(self, speed):
        super().__init__()
        self._player = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png"))
        self._player = pygame.transform.smoothscale(
            self._player, (20, 20))
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.screen_rect = self._screen.get_rect()
        self._speed = speed
        self.rect = self._player.get_rect()
        self.rect.x = 340
        self.rect.y = 460
        self._events = HandleEvents()
        self._maze = Level(self._screen)


    def _move_player(self, direction, opposite=False):
        if opposite:
            if direction == "l":
                self.rect.x += self._speed
            if direction == "r":
                self.rect.x -= self._speed
            if direction == "u":
                self.rect.y += self._speed
            if direction == "d":
                self.rect.y -= self._speed
        else:
            if direction == "l":
                self.rect.x -= self._speed
            if direction == "r":
                self.rect.x += self._speed
            if direction == "u":
                self.rect.y -= self._speed
            if direction == "d":
                self.rect.y += self._speed
