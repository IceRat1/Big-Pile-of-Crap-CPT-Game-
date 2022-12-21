import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

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
        self.p1x_velo = 0
        self.p1y_velo = 0

        self.player2x = 400
        self.player2y = 400
        self.p2x_velo = 0
        self.p2y_velo = 0

        self.running = True

    def event_getter(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False

    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.p1x_velo < 5:
                self.p1x_velo += 1
        if keys[pygame.K_s]:
            pass
        if keys[pygame.K_a]:
            pass
        if keys[pygame.K_d]:
            pass

    def waluigitrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((128, 0, 128))


            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def meadowstrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((0, 0, 0))


            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def mariotrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((178, 0, 0))


            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def run(self) -> None:
        track = random.randrange(0, 3)
        print(track)
        if track == 0:
            pygame.mixer.music.load("Waluigi Pinball - Mario Kart DS - Super Smash Bros. Ultimate.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            kartgame.waluigitrack(self)
        elif track == 1:
            pygame.mixer.music.load("Moo Moo Meadows - Mario Kart Wii.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            kartgame.meadowstrack(self)
        else:
            pygame.mixer.music.load("Super Mario Kart Music (SNES) - Mario Circuit.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            kartgame.mariotrack(self)

if __name__ == "__main__":
    game = kartgame()
    game.run()
