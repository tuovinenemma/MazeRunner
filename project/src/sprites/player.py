import os
import pygame
from events import HandleEvents
from level import Level

dirname = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):

    def __init__(self, speed):
        self._playerone = pygame.image.load(
            os.path.join(dirname, "..", "assets", "player.png"))
        self._playerone = pygame.transform.smoothscale(
            self._playerone, (25, 25))
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))
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

    def _player_collision(self, key_pressed):
        key_pressed = self._events._key_pressed
        self._move_player(key_pressed)
        collision = pygame.sprite.spritecollide(
            self._playerone, self._maze._walls, False)
        if collision:
            self._move_player(key_pressed, collision=True)
            self._move_player(self._key)
            collision = pygame.sprite.spritecollide(
                self._playerone, self._maze._walls, False)
            if collision:
                self._move_player(self._key, collision=True)
                self._key = "0"
            return
        self._key = key_pressed

        if self.rect.x < 0:
            self.rect.x = 700
            self._screen.blit(self._playerone, (self.rect.x, self.rect.y))

        elif self.rect.x > 700:
            self.rect.x = 0
            self._screen.blit(self._playerone, (self.rect.x, self.rect.y))
