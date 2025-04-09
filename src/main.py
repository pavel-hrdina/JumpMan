import pygame


class MainGame:
    """
    The main game class that runs the game
    and takes care of initialization and
    cleanup
    """

    def __init__(self, size):
        """
        You don't know what init does, lol.
        :param size: tuple of int
        """
        self._running = True
        self._display_surface = None
        self.size = size  # tuple of 2 nums

    def on_init(self):
        """
        takes care of game initialization
        :return: None
        """
        pygame.init()
        self._display_surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._running = True

    def on_event(self, event):
        """
        in case the player wants to quit the game, this method is called
        :param event:
        :return: None
        """
        if event.type == pygame.QUIT:
            self._running = False

    def clenup(self):
        """
        exits the game and clens up
        :return: None
        """
        pygame.quit()

    def run(self):
        """
        runs the game
        :return: None
        """
        if not self.on_init():
            self._running = True

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
        self.clenup()


if __name__ == "__main__":
    game = MainGame((640, 480))
    game.run()
