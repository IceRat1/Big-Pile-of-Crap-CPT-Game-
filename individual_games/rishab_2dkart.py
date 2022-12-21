import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------

# ---------------------------

class kartgame():
    def __init__(self) -> None:
        self.player1x = 200
        self.player1y = 200
        self.player2x = 400
        self.player2y = 400
        self.running = True

    def event_getter():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

    def run():
        running = True
        while running:
            

            # GAME STATE UPDATES
            # All game math and comparisons happen here

            # DRAWING
            screen.fill((255, 255, 255))  # always the first drawing command

            

            # Must be the last two lines
            # of the game loop
            pygame.display.flip()
            clock.tick(30)
            #---------------------------


    pygame.quit()

if __name__ == "__main__":
    game = kartgame()
    game.run()
