import os
import pygame
from events import HandleEvents
from level import Level

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):

    def __init__(self, speed):
        super().__init__()
        self._playerone = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png"))
        self._playerone = pygame.transform.smoothscale(
            self._playerone, (25, 25))
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.screen_rect = self._screen.get_rect()
        self._speed = speed
        self.rect = self._playerone.get_rect()
        self.rect.x = 323
        self.rect.y = 625
        self._key = "0"
        self._events = HandleEvents()
        self._maze = Level(self._screen)

    def _move_player(self, direction, collision=None):
        if collision:
            if direction == "l":
                self.rect.x -= 1
            if direction == "r":
                self.rect.x += 1
            if direction == "u":
                self.rect.y -= 1
            if direction == "d":
                self.rect.y += 1
        else:
            if direction == "l":
                self.rect.x -= self._speed
            if direction == "r":
                self.rect.x += self._speed
            if direction == "u":
                self.rect.y -= self._speed
            if direction == "d":
                self.rect.y += self._speed

    def _render_player(self, screen):
        screen.blit(self._playerone, (self.rect.x, self.rect.y))




