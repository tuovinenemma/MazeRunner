import sys
import pygame


class GameOver:
    def __init__(self, clock, events):

        pygame.init()
        self._clock = clock
        self._state = "game over"
        self._width = 700
        self._height = 875
        self._events = events
        self._screen = pygame.display.set_mode((self._width, self._height))

    def _end_game(self):
        self._end_text2()
        pygame.display.update()

    def _end_screen(self):
        self._end_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "restart":
                return
            if self._events._key_pressed == "exit":
                sys.exit()
            self._render()
            pygame.display.update()
            self._clock.tick(60)

    def _game_ending(self):
        if self._state == "game over":
            self._ending()

    def _render(self):
        self._end_text2()

    def _end_text1(self, words, screen, pos, size, colour, font_name, middle=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _end_text2(self):
        self._screen.fill((255, 255, 255))
        self._end_text1('PRESS "R" TO RESTART THE GAME', self._screen, [
                        self._width//2, self._height//2+400], 30, (0, 0, 0), 'arial black', middle=True)
        self._end_text1('PRESS "E" TO EXIT THE GAME', self._screen, [
                        self._width//2, self._height//2+350], 30, (0, 0, 0), 'arial black', middle=True)
        self._end_text1('GAME OVER', self._screen, [
                        self._width//2, self._height//2-50], 45, (0, 0, 0), 'arial black', middle=True)
