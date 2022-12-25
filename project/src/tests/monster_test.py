import unittest
import pygame
from sprites.monster import Monster

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster = Monster()
        self.maze_walls = pygame.sprite.Group()
        self.wall1 = pygame.sprite.Sprite()
        self.wall1.rect = pygame.Rect(100, 100, 25, 25)
        self.maze_walls.add(self.wall1)
        self.screen = pygame.display.set_mode((700, 875))

    def test_monster_can_move_right(self):
        self.monster._move_monster(direction=2)
        self.assertEqual(self.monster.rect.x, 326)

    def test_monster_can_move_left(self):
        self.monster._move_monster(direction=1)
        self.assertEqual(self.monster.rect.x, 324)

    def test_monster_can_move_up(self):
        self.monster._move_monster(direction=4)
        self.assertEqual(self.monster.rect.y, 411)

    def test_monster_can_move_down(self):
        self.monster._move_monster(direction=3)
        self.assertEqual(self.monster.rect.y, 409)

    def test_open_turns_returns_different_directions_for_directions_1_2(self):
        self.monster._monster_direction = 1
        turns = self.monster._open_turns(self.monster._monster_direction)
        self.assertEqual(len(turns), 2)
        self.assertNotEqual(turns[0], turns[1])
        self.monster._monster_direction = 2
        turns = self.monster._open_turns(self.monster._monster_direction)
        self.assertEqual(len(turns), 2)
        self.assertNotEqual(turns[0], turns[1])

    def test_open_turns_returns_different_directions_for_directions_3_4(self):
        self.monster._monster_direction = 3
        turns = self.monster._open_turns(self.monster._monster_direction)
        self.assertEqual(len(turns), 2)
        self.assertNotEqual(turns[0], turns[1])
        self.monster._monster_direction = 4
        turns = self.monster._open_turns(self.monster._monster_direction)
        self.assertEqual(len(turns), 2)
        self.assertNotEqual(turns[0], turns[1])

    def test_move_monster_moves_in_correct_direction(self):
        self.monster._move_monster(direction=1)
        self.assertEqual(self.monster.rect.x, 324)
        self.monster._move_monster(direction=2)
        self.assertEqual(self.monster.rect.x, 325)
        self.monster._move_monster(direction=3)
        self.assertEqual(self.monster.rect.y, 409)
        self.monster._move_monster(direction=4)
        self.assertEqual(self.monster.rect.y, 410)

    def test_move_monster_moves_in_opposite_direction(self):
        self.monster._move_monster(direction=1, opposite=True)
        self.assertEqual(self.monster.rect.x, 326)
        self.monster._move_monster(direction=2, opposite=True)
        self.assertEqual(self.monster.rect.x, 325)
        self.monster._move_monster(direction=3, opposite=True)
        self.assertEqual(self.monster.rect.y, 411)
        self.monster._move_monster(direction=4, opposite=True)
        self.assertEqual(self.monster.rect.y, 410)


    def test_find_direction_returns_current_direction_when_0(self):
        self.monster._monster_direction = 0

    def test_monster_starts_at_random_location(self):
        self.assertNotEqual(self.monster.rect.x, self.monster.rect.y)
        

