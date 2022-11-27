import pygame

class Start:
    def __init__(self, events, clock):
        pygame.init()
        self._clock = clock
        self._state = "start"
        self._width = 700
        self._height = 875
        self._events = events
        self._screen = pygame.display.set_mode((self._width, self._height))

    def _start_game(self):
        self._start_text2()
        pygame.display.update()

    def _start_screen(self):
        self._start_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "space":
                return
            pygame.display.update()
            self._clock.tick(60)

    def _game_starting(self):
        if self._state == "start":
            self._starting()

    def _render(self):

        self._start_text2()

    def _start_text1(self, words, screen, pos, size, colour, font_name, middle=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _start_text2(self):
        pygame.mouse.set_visible(0)
        self._screen.fill((255, 255, 255))
        self._start_text1('PRESS SPACE BAR TO ENTER THE MAZE', self._screen, [self._width//2, self._height//2-40], 30, (0, 0, 0), 'arial black', middle=True)
        self._start_text1('THE MAZE RUNNER', self._screen, [self._width//2, self._height//2-150], 45, (0, 0, 0), 'arial black', middle=True)
