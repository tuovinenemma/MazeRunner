import os
from random import randint
import pygame
dirname = os.path.dirname(__file__)

class Monster(pygame.sprite.Sprite):
    """Konstruktori luo vihollisen
    """

    def __init__(self):
        super().__init__()

        self._monster = pygame.image.load(os.path.join(dirname, "..", "assets", "monster.png"))
        self._monster = pygame.transform.smoothscale(self._monster, (25, 25))
        self.image = self._monster
        self._speed = 2
        self.rect = self._monster.get_rect()
        self.rect.x = 325
        self.rect.y = 410
        self._monster_direction = 3
        self._maze_walls = None

    def _monster_can_move(self, maze_walls):
        """Huolehtii vihollisen liikkumisesta
        """
        self._maze_walls = maze_walls
        if self.rect.y < 60:
            self.rect.y = 930
            self.rect.x = 390
        if self.rect.y > 930:
            self.rect.y = 60
            self.rect.x = 390
        dir = self._find_direction()
        self._move_monster(dir)
        collision = pygame.sprite.spritecollide(self, maze_walls, False)
        if collision:
            self._move_monster(dir, opposite=True)
            self._move_monster(self._monster_direction)
            collision = pygame.sprite.spritecollide(self, maze_walls, False)
            if collision:
                self._move_monster(self._monster_direction, opposite=True)
                self._monster_direction = 0
            return
        self._monster_direction = dir

    def _find_direction(self):
        dir = self._open_directions()
        number = randint(0,1)
        if self._monster_direction == 0:
            return dir
        elif number == 0:
            return dir
        return self._monster_direction

    def _open_directions(self):
        turn = self._open_turns(self._monster_direction)
        for direction in turn:
            self._move_monster(direction)
            collision = pygame.sprite.spritecollide(self, self._maze_walls, False)
            if not collision:
                self._move_monster(direction, opposite=True)
                return direction
            self._move_monster(direction, opposite=True)
        return self._monster_direction

    def _open_turns(self, direction):
        number = randint(0,1)
        if direction == 1:
            turns = [[3, 4], [4, 3]]
            return turns[number]
        elif direction == 2:
            turns = [[3, 4], [4, 3]]
            return turns[number]
        elif direction == 4:
            turns = [[1, 2], [2, 1]]
            return turns[number]
        elif direction == 3:
            turns = [[1, 2], [2, 1]]
            return turns[number]
        elif direction == 0:
            return [randint(1, 4), randint(1, 4)]

    def _move_monster(self, direction, opposite=False):
        speed = 1
        if opposite:
            if direction == 1:
                self.rect.x += speed
            if direction == 2:
                self.rect.x -= speed
            if direction == 3:
                self.rect.y += speed
            if direction == 4:
                self.rect.y -= speed
        else:
            if direction == 1:
                self.rect.x -= speed
            if direction == 2:
                self.rect.x += speed
            if direction == 3:
                self.rect.y -= speed
            if direction == 4:
                self.rect.y += speed
