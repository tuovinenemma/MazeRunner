import os
import pygame
dirname = os.path.dirname(__file__)


class Level:
    def __init__(self, screen):
        self._screen = screen
        self._all_units = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._moss = pygame.sprite.Group()
        self._paths = pygame.sprite.Group()
        self._moss2 = pygame.sprite.Group()

    def _create_maze(self):

        unit_size = 25
        maze = MAZE_ONE
        width, height = len(maze[0]), len(maze)
        for x in range(width):
            for y in range(height):
                unit = maze[y][x]
                x_axis = x * unit_size
                y_axis = y * unit_size
                self._add_units(unit, x_axis, y_axis)

        self._group_units()

    def _group_units(self):

        self._all_units.add(self._paths, self._walls, self._moss, self._moss2)

    def _add_units(self, unit, x, y):
        if unit == 1:
            self._walls.add(Wall(x, y))
        else:
            if unit == 0:
                self._paths.add(Path(x, y))
            if unit == 2:
                self._paths.add(Path(x, y))

            if unit == 3:
                self._paths.add(Moss(x, y))

            if unit == 4:
                self._paths.add(Moss2(x, y))

    def _make_maze(self):

        self._all_units.draw(self._screen)


class Path(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((1, 50, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Moss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((17, 66, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Moss2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 76, 56))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


MAZE_ONE = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 4, 1, 3, 1, 3, 4, 4, 3, 1, 1, 4, 4, 1, 4,
                3, 1, 3, 4, 4, 3, 3, 1, 3, 4, 4, 1, 1],
            [1, 4, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1,
             0, 3, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 1],
            [3, 0, 0, 0, 3, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1,
             0, 1, 0, 4, 3, 4, 1, 0, 4, 0, 0, 0, 1],
            [3, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 3, 0, 1, 3, 3, 1, 0, 1, 0, 3, 0, 1],
            [1, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 1, 0, 3,
             0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 4, 0, 3, 0, 0, 0, 1, 1, 1, 0, 1,
             0, 3, 0, 3, 1, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 3, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0,
             0, 1, 0, 1, 1, 3, 0, 3, 4, 0, 3, 1, 1],
            [1, 0, 0, 0, 3, 0, 1, 1, 1, 0, 1, 1, 3, 0, 1,
             0, 1, 0, 4, 0, 1, 0, 4, 4, 0, 0, 0, 3],
            [4, 0, 1, 0, 3, 0, 3, 0, 0, 0, 3, 1, 4, 0, 3,
             0, 3, 0, 3, 0, 3, 0, 1, 1, 0, 1, 1, 3],
            [3, 0, 1, 0, 1, 0, 3, 1, 4, 0, 3, 3, 3, 0, 1,
             0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 1, 0, 3],
            [3, 1, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1, 1, 0, 0,
             0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 3, 0, 1],
            [3, 1, 0, 4, 1, 0, 1, 0, 3, 0, 3, 4, 3, 0, 1,
             1, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0, 0, 1],
            [1, 1, 0, 3, 1, 0, 3, 1, 4, 1, 1, 4, 1, 0, 3,
             0, 0, 1, 0, 3, 0, 4, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 3, 3, 0, 0, 0, 4, 0, 3, 4, 3, 0, 3,
             0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [4, 1, 0, 1, 3, 0, 1, 0, 1, 0, 3, 1, 3, 0, 1,
             0, 1, 1, 1, 1, 0, 3, 0, 3, 4, 3, 0, 3],
            [4, 1, 0, 4, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 1],
            [3, 1, 0, 1, 3, 3, 3, 4, 4, 1, 0, 1, 0, 0, 0,
             0, 1, 1, 1, 0, 3, 3, 4, 3, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
             0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0,
             0, 1, 1, 1, 0, 1, 3, 1, 0, 1, 3, 0, 3],
            [3, 1, 0, 0, 0, 1, 0, 1, 1, 4, 4, 1, 0, 3, 3,
             1, 1, 1, 4, 0, 3, 1, 3, 0, 3, 1, 0, 1],
            [3, 1, 1, 1, 0, 3, 0, 4, 0, 0, 0, 4, 0, 1, 1,
             0, 0, 0, 4, 0, 3, 1, 1, 0, 1, 1, 0, 1],
            [3, 1, 1, 1, 0, 3, 0, 4, 0, 1, 0, 4, 0, 1, 1,
             0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 1,
             0, 1, 0, 1, 3, 4, 3, 1, 0, 3, 3, 0, 3],
            [4, 0, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3],
            [1, 0, 1, 4, 1, 1, 4, 1, 1, 0, 1, 0, 1, 0, 1,
             0, 1, 1, 3, 3, 1, 3, 4, 1, 4, 1, 0, 3],
            [1, 0, 0, 0, 0, 0, 3, 3, 1, 0, 1, 1, 1, 1, 1,
             0, 3, 0, 0, 0, 0, 1, 4, 4, 0, 3, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,
             0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 3, 0, 1],
            [3, 1, 1, 1, 0, 1, 0, 4, 3, 1, 0, 3, 1, 3, 1,
             3, 3, 1, 1, 3, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 4, 0, 1, 0, 3, 0, 0, 0,
             3, 0, 0, 0, 3, 0, 3, 0, 1, 0, 3, 0, 1],
            [3, 0, 3, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4, 0,
             1, 0, 1, 0, 1, 0, 3, 0, 4, 0, 1, 1, 3],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
             0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [3, 1, 4, 4, 1, 1, 3, 3, 4, 3, 3, 3, 4, 1, 4, 3, 1, 1, 4, 4, 1, 1, 4, 4, 1, 1, 1, 1]]
