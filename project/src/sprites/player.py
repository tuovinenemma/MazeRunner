import pygame
import os
from events import *

dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):

    def __init__(self, speed, image=None):

        self._playerone = pygame.image.load(os.path.join(dirname, "..", "assets", "player.png"))
        self._playerone = pygame.transform.smoothscale(self._playerone, (25, 25))
        self._speed = speed
        self.rect = self._playerone.get_rect()
        self.rect.x = 323
        self.rect.y = 625
        self._events = HandleEvents()