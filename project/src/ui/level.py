import os
import pygame
dirname = os.path.dirname(__file__)


class Level:
    """Pelin kentästä vastaava näkymä
    """
    def __init__(self, screen):
        """Luokan konstruktori
        """
        self._screen = screen
        self._all_units = pygame.sprite.Group()
        self._all_walls = pygame.sprite.Group()
        self._all_walls_2 = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._moss = pygame.sprite.Group()
        self._paths = pygame.sprite.Group()
        self._moss2 = pygame.sprite.Group()
        self._exit = pygame.sprite.Group()
        self._treasures = pygame.sprite.Group()
        self._sand = pygame.sprite.Group()
        self._sand2 = pygame.sprite.Group()
        self._sand3 = pygame.sprite.Group()

    def _create_maze(self):
        """Luo ensimmäisen kentän
        """
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

    def _create_maze_two(self):
        """Luo toisen kentän
        """
        unit_size = 25
        maze = MAZE_TWO
        width, height = len(maze[0]), len(maze)
        for x in range(width):
            for y in range(height):
                unit = maze[y][x]
                x_axis = x * unit_size
                y_axis = y * unit_size
                self._add_units(unit, x_axis, y_axis)

        self._group_units()

    def _group_units(self):

        self._all_units.add(self._paths, self._walls, self._moss, self._moss2, self._treasures, self._exit, self._sand, self._sand2, self._sand3)
        self._all_walls.add(self._walls, self._moss, self._moss2)
        self._all_walls_2.add(self._sand, self._sand2, self._sand3)

    def _add_units(self, unit, x, y):
        """Lisää objektit kentälle
        """
        if unit == 1:
            self._walls.add(Wall(x, y))
        else:
            if unit == 0:
                self._paths.add(Path(x, y))
            if unit == 2:
                self._paths.add(Path(x, y))

            if unit == 3:
                self._moss.add(Moss(x, y))

            if unit == 4:
                self._moss2.add(Moss2(x, y))

            if unit == 5:
                self._paths.add(Path(x, y))
                self._treasures.add(Treasure(x, y))

            if unit == 6:
                self._paths.add(Path(x, y))
                self._exit.add(Exit(x, y))

            if unit == 7:
                self._sand.add(Sand(x, y))

            if unit == 8:
                self._sand2.add(Sand2(x, y))

            if unit == 9:
                self._sand2.add(Sand2(x, y))
            



class Path(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden polun.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden seinän.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((1, 50, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Moss(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden seinän.
    """
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
        """Luokan konstruktori. Luo uuden seinän.
        """
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((0, 76, 56))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Treasure(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden aarteen.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "..", "assets", "treasure.png"))
        self.image = pygame.transform.smoothscale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Exit(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uloskäynnin.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((31, 32, 34))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sand(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden seinän.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((53, 33, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sand2(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden seinän.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((66, 40, 14))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sand3(pygame.sprite.Sprite):
    """Luokan konstruktori. Luo uuden seinän.
    """
    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((25, 25))
        self.image = image
        self.image.fill((83, 54, 33))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


MAZE_ONE = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 4, 1, 3, 1, 3, 4, 4, 3, 1, 1, 4, 4, 1, 4, 3, 1, 3, 4, 4, 3, 3, 1, 3, 4, 4, 1, 1],
            [1, 4, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 5, 1, 1, 3, 3, 1],
            [3, 0, 0, 0, 3, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 4, 3, 4, 1, 0, 4, 0, 0, 0, 1],
            [3, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 3, 3, 1, 0, 1, 0, 3, 0, 1],
            [1, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 1, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 4, 0, 3, 0, 0, 0, 1, 1, 1, 0, 1, 0, 3, 0, 3, 1, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 3, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 3, 0, 3, 4, 0, 3, 1, 1],
            [1, 0, 0, 0, 3, 0, 1, 1, 1, 0, 1, 1, 3, 0, 1, 0, 1, 0, 4, 0, 1, 0, 4, 4, 0, 0, 0, 3],
            [4, 0, 1, 0, 3, 0, 3, 0, 0, 0, 3, 1, 4, 0, 3, 0, 3, 0, 3, 0, 3, 0, 1, 1, 0, 1, 1, 3],
            [3, 5, 1, 0, 1, 0, 3, 1, 4, 0, 3, 3, 3, 0, 1, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 1, 0, 3],
            [3, 1, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 3, 0, 1],
            [3, 1, 0, 4, 1, 0, 1, 0, 3, 0, 3, 4, 3, 0, 1, 1, 0, 0, 0, 0, 0, 4, 3, 4, 0, 0, 0, 1],
            [1, 1, 0, 3, 1, 0, 3, 1, 4, 1, 1, 4, 1, 0, 3, 0, 0, 1, 0, 3, 0, 4, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 3, 3, 0, 0, 0, 4, 0, 3, 4, 3, 0, 3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [4, 1, 0, 1, 3, 0, 1, 0, 1, 0, 3, 1, 3, 0, 1, 0, 1, 1, 1, 1, 0, 3, 0, 3, 4, 3, 0, 3],
            [4, 1, 0, 4, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 1],
            [3, 1, 0, 1, 3, 3, 3, 4, 4, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 3, 3, 4, 3, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 3, 1, 0, 1, 3, 0, 3],
            [3, 1, 0, 0, 0, 1, 0, 1, 1, 4, 4, 1, 0, 3, 3, 1, 1, 1, 4, 0, 3, 1, 3, 0, 3, 1, 0, 1],
            [3, 1, 1, 1, 0, 3, 0, 4, 0, 0, 0, 4, 0, 1, 1, 0, 0, 0, 4, 0, 3, 1, 1, 0, 1, 1, 0, 1],
            [3, 1, 1, 1, 0, 3, 0, 4, 0, 1, 0, 4, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 1, 0, 1, 0, 1, 3, 4, 3, 1, 0, 3, 3, 0, 3],
            [4, 0, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3],
            [1, 0, 1, 4, 1, 1, 4, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 3, 3, 1, 3, 4, 1, 4, 1, 0, 3],
            [1, 0, 0, 0, 0, 0, 3, 3, 1, 0, 1, 1, 1, 1, 1, 0, 3, 0, 0, 0, 0, 1, 4, 4, 0, 3, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 3, 0, 1],
            [3, 1, 1, 1, 0, 1, 0, 4, 3, 1, 0, 3, 1, 3, 1, 3, 3, 1, 1, 3, 0, 0, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 4, 0, 1, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 1, 0, 3, 5, 1],
            [3, 0, 3, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4, 0, 1, 0, 1, 0, 1, 0, 3, 0, 4, 0, 1, 1, 3],
            [4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 6],
            [3, 1, 4, 4, 1, 1, 3, 3, 4, 3, 3, 3, 4, 1, 4, 3, 1, 1, 4, 4, 1, 1, 4, 4, 1, 1, 1, 1]]

MAZE_TWO = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [7, 9, 7, 8, 7, 8, 9, 9, 8, 7, 7, 9, 9, 7, 9, 8, 7, 8, 9, 9, 8, 8, 7, 8, 9, 9, 7, 7],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 7],
            [8, 5, 8, 0, 8, 0, 7, 7, 5, 7, 7, 7, 7, 0, 7, 5, 7, 0, 9, 8, 9, 7, 0, 9, 0, 0, 5, 7],
            [8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8, 0, 9, 8, 8, 7, 0, 7, 0, 8, 0, 7],
            [7, 0, 9, 0, 8, 0, 9, 0, 7, 0, 7, 0, 7, 0, 8, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 8, 0, 7],
            [7, 0, 9, 6, 9, 0, 8, 0, 9, 0, 7, 0, 7, 0, 7, 0, 0, 0, 8, 0, 7, 0, 7, 7, 0, 0, 0, 7],
            [7, 0, 7, 7, 8, 0, 0, 0, 9, 0, 7, 0, 0, 0, 0, 0, 7, 0, 7, 0, 8, 0, 8, 9, 0, 8, 0, 7],
            [7, 0, 8, 0, 8, 0, 7, 7, 7, 0, 0, 0, 8, 0, 7, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8],
            [9, 0, 7, 0, 8, 0, 5, 0, 0, 0, 7, 0, 9, 0, 8, 0, 0, 0, 8, 0, 8, 0, 7, 7, 0, 7, 0, 8],
            [8, 0, 0, 0, 7, 0, 8, 7, 9, 0, 0, 0, 0, 0, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0, 5, 9, 0, 8],
            [8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 0, 0, 0, 8, 0, 7, 0, 7, 7, 0, 7, 0, 8, 0, 7],
            [8, 7, 0, 9, 7, 0, 7, 0, 8, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 8, 0, 9, 7, 7, 0, 7, 0, 8, 0, 0, 7, 0, 8, 0, 9, 0, 7, 0, 7, 0, 7],
            [7, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 7, 0, 7, 0, 0, 0, 7, 0, 9, 0, 7],
            [9, 0, 0, 0, 0, 0, 7, 0, 7, 0, 8, 7, 8, 0, 7, 0, 7, 7, 0, 7, 0, 8, 0, 8, 0, 8, 0, 8],
            [9, 0, 9, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 8, 0, 0, 0, 0, 0, 7],
            [8, 0, 8, 7, 8, 8, 8, 9, 9, 7, 0, 7, 7, 0, 0, 0, 7, 0, 7, 0, 8, 8, 9, 8, 0, 7, 0, 7],
            [7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 7],
            [7, 7, 0, 7, 0, 7, 0, 7, 0, 7, 8, 7, 8, 0, 7, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 8, 0, 8],
            [7, 0, 0, 0, 0, 7, 0, 0, 0, 9, 9, 7, 8, 0, 8, 0, 7, 0, 9, 9, 8, 0, 8, 5, 0, 0, 0, 7],
            [7, 8, 7, 7, 0, 8, 0, 9, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 9, 0, 8, 0, 7, 0, 7, 0, 9, 7],
            [7, 0, 7, 7, 0, 8, 0, 0, 0, 7, 0, 9, 9, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 9, 0, 0, 8],
            [7, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 7, 0, 7, 8, 9, 0, 7, 0, 8, 8, 0, 8],
            [7, 0, 9, 9, 0, 7, 0, 9, 0, 0, 0, 8, 0, 7, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8],
            [7, 0, 7, 0, 0, 7, 9, 7, 0, 9, 0, 0, 0, 0, 0, 0, 7, 7, 0, 8, 7, 8, 0, 7, 0, 7, 0, 8],
            [7, 0, 0, 0, 8, 9, 8, 8, 0, 8, 0, 7, 7, 0, 7, 0, 8, 0, 0, 9, 0, 7, 0, 9, 0, 0, 0, 7],
            [7, 7, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 9, 0, 7, 0, 8, 0, 7],
            [7, 7, 0, 7, 0, 7, 0, 9, 8, 7, 0, 8, 7, 8, 7, 8, 0, 7, 7, 8, 0, 9, 0, 0, 0, 0, 0, 7],
            [7, 5, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8, 0, 0, 0, 8, 0, 0, 0, 8, 0, 7, 0, 7, 7, 7, 0, 7],
            [7, 0, 9, 8, 9, 7, 0, 7, 0, 0, 0, 7, 0, 9, 0, 7, 0, 7, 0, 0, 0, 8, 0, 9, 9, 7, 0, 8],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 5, 7],
            [7, 7, 7, 7, 7, 7, 7, 8, 9, 8, 8, 8, 9, 7, 9, 8, 7, 7, 9, 9, 7, 7, 9, 9, 7, 7, 7, 7]]


MAZE_THREE = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [7, 9, 7, 8, 7, 8, 9, 9, 8, 7, 7, 9, 9, 7, 9, 8, 7, 8, 9, 9, 8, 8, 7, 8, 9, 9, 7, 7],
            [7, 0, 0, 0, 8, 0, 8, 8, 0, 9, 0, 0, 0, 0, 7, 0, 8, 0, 0, 0, 0, 0, 5, 7, 7, 8, 8, 7],
            [8, 0, 8, 0, 8, 0, 7, 7, 0, 7, 7, 7, 7, 0, 7, 0, 7, 0, 9, 8, 9, 7, 0, 9, 0, 0, 0, 7],
            [8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 7, 0, 7, 0, 8, 0, 7],
            [7, 0, 9, 0, 8, 0, 0, 0, 7, 0, 7, 0, 7, 0, 8, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 8, 0, 7],
            [7, 0, 9, 0, 9, 0, 8, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 8, 0, 7, 0, 7, 7, 0, 0, 0, 7],
            [7, 0, 7, 7, 8, 0, 0, 0, 9, 0, 7, 0, 0, 0, 0, 0, 7, 0, 7, 0, 8, 0, 8, 9, 0, 8, 0, 7],
            [7, 0, 8, 0, 8, 0, 7, 7, 7, 0, 0, 0, 8, 0, 7, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8],
            [9, 0, 7, 0, 8, 0, 0, 0, 0, 0, 7, 0, 9, 0, 0, 0, 0, 0, 8, 0, 8, 0, 7, 7, 0, 7, 7, 8],
            [8, 0, 0, 0, 7, 0, 8, 7, 9, 0, 0, 0, 0, 0, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
            [8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 0, 0, 0, 8, 0, 7, 0, 7, 7, 0, 7, 0, 8, 0, 7],
            [8, 7, 0, 9, 7, 0, 7, 0, 8, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 8, 0, 9, 7, 7, 0, 7, 0, 8, 0, 0, 7, 0, 8, 0, 9, 0, 7, 0, 7, 0, 7],
            [7, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [9, 0, 0, 0, 0, 0, 7, 0, 7, 0, 8, 7, 8, 0, 7, 0, 7, 7, 0, 7, 0, 8, 0, 8, 0, 8, 0, 8],
            [9, 0, 9, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 7],
            [8, 0, 8, 7, 8, 8, 8, 9, 9, 7, 0, 7, 7, 0, 0, 0, 7, 0, 7, 0, 8, 8, 9, 8, 0, 7, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 7],
            [7, 7, 0, 7, 0, 7, 0, 7, 0, 7, 8, 7, 8, 0, 7, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 8, 9, 8],
            [7, 0, 0, 0, 0, 7, 0, 0, 0, 9, 9, 7, 8, 0, 8, 0, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 7],
            [7, 8, 7, 7, 0, 8, 0, 9, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 9, 0, 8, 0, 7, 0, 7, 0, 9, 7],
            [7, 0, 7, 7, 0, 8, 0, 0, 0, 7, 0, 9, 9, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 8],
            [7, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 7, 0, 7, 8, 9, 0, 7, 0, 8, 8, 0, 8],
            [7, 0, 9, 9, 0, 7, 0, 0, 0, 0, 0, 8, 0, 7, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
            [7, 0, 7, 0, 0, 7, 9, 7, 0, 9, 0, 0, 0, 0, 0, 0, 7, 7, 0, 8, 7, 8, 0, 7, 0, 7, 0, 8],
            [7, 0, 0, 0, 8, 9, 8, 8, 0, 8, 0, 7, 7, 0, 7, 0, 8, 0, 0, 9, 0, 7, 0, 9, 0, 0, 0, 7],
            [7, 7, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 7, 0, 8, 0, 7],
            [7, 7, 0, 7, 0, 7, 0, 9, 8, 7, 0, 8, 7, 8, 7, 8, 0, 7, 7, 8, 0, 9, 0, 0, 0, 0, 0, 7],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8, 0, 0, 0, 8, 0, 0, 0, 8, 0, 0, 0, 7, 0, 8, 0, 7],
            [7, 0, 9, 0, 9, 7, 0, 7, 0, 0, 0, 7, 0, 9, 0, 7, 0, 7, 0, 0, 0, 8, 0, 0, 0, 0, 0, 8],
            [7, 0, 0, 0, 0, 0, 0, 7, 0, 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 8, 0, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 8, 9, 8, 8, 8, 9, 7, 9, 8, 7, 7, 9, 9, 7, 7, 9, 9, 7, 7, 7, 7]]
