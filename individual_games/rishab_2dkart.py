import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 960
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class kartgame():
    def __init__(self) -> None:
        self.player1x = 100
        self.player1y = 200
        self.p1x_velo = 0
        self.p1y_velo = 0
        self.p1_max = 3
        self.slowdown1x = True
        self.slowdown1y = True
        self.x1_start_ticks = 0
        self.y1_start_ticks = 0
        
        self.player2x = 200
        self.player2y = 200
        self.p2x_velo = 0
        self.p2y_velo = 0
        self.p2_max = 3
        self.slowdown2x = True
        self.slowdown2y = True
        self.x2_start_ticks = 0
        self.y2_start_ticks = 0

        self.p1_kart = pygame.image.load("mario_topsprite.png")
        self.p1_kart = pygame.transform.scale(self.p1_kart, (30, 30))
        self.p1rot= pygame.transform.rotate(self.p1_kart, 0)
        self.p2_kart = pygame.image.load("luigi_topsprite.png")
        self.p2_kart = pygame.transform.scale(self.p2_kart, (30, 30))
        self.p2rot= pygame.transform.rotate(self.p2_kart, 0)
        self.running = True

    def event_getter(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False

    def karts(self) -> None:
        p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
        p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
        self.player1x += self.p1x_velo
        self.player1y += self.p1y_velo
        self.player2x += self.p2x_velo
        self.player2y += self.p2y_velo
        screen.blit(self.p1rot, p1new_rect)
        screen.blit(self.p2rot, p2new_rect)
        p1_kart = pygame.Rect((self.player1x, self.player1y, 30, 30))
        p2_kart = pygame.Rect((self.player2x, self.player2y, 30, 30))
        kart_collide = pygame.Rect.colliderect(p1_kart, p2_kart)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                if self.p1y_velo > -self.p1_max:
                    self.p1y_velo -= 0.1
                else:
                    self.p1y_velo = -self.p1_max
                self.p1y_velo = round(self.p1y_velo, 2)
                self.slowdown1y = False
        if keys[pygame.K_s]:
                if self.p1y_velo < self.p1_max:
                    self.p1y_velo += 0.1
                else:
                    self.p1y_velo = self.p1_max
                self.p1y_velo = round(self.p1y_velo, 2)
                self.slowdown1y = False
        if keys[pygame.K_a]:
                if self.p1x_velo > -self.p1_max:
                    self.p1x_velo -= 0.1
                else:
                    self.p1x_velo = -self.p1_max
                self.p1x_velo = round(self.p1x_velo, 2)
                self.slowdown1x = False
        if keys[pygame.K_d]:
                if self.p1x_velo < self.p1_max:
                    self.p1x_velo += 0.1
                else:
                    self.p1x_velo = self.p1_max
                self.p1x_velo = round(self.p1x_velo, 2)
                self.slowdown1x = False
        if keys[pygame.K_UP]:
                if self.p2y_velo > -self.p2_max:
                    self.p2y_velo -= 0.1
                else:
                    self.p2y_velo = -self.p2_max
                self.p2y_velo = round(self.p2y_velo, 2)
                self.slowdown2y = False
        if keys[pygame.K_DOWN]:
                if self.p2y_velo < self.p2_max:
                    self.p2y_velo += 0.1
                else:
                    self.p2y_velo = self.p2_max
                self.p2y_velo = round(self.p2y_velo, 2)
                self.slowdown2y = False
        if keys[pygame.K_LEFT]:
                if self.p2x_velo > -self.p2_max:
                    self.p2x_velo -= 0.1
                else:
                    self.p2x_velo = -self.p2_max
                self.p2x_velo = round(self.p2x_velo, 2)
                self.slowdown2x = False
        if keys[pygame.K_RIGHT]:
                if self.p2x_velo < self.p2_max:
                    self.p2x_velo += 0.1
                else:
                    self.p2x_velo = self.p2_max
                self.p2x_velo = round(self.p2x_velo, 2)
                self.slowdown2x = False

        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            if not self.slowdown1y:
                self.slowdown1y = True
                self.y1_start_ticks = pygame.time.get_ticks()
            y1_seconds = (pygame.time.get_ticks() - self.y1_start_ticks)/1000
            if y1_seconds > 1:
                self.p1y_velo = 0
            if self.p1y_velo > 0:
                self.p1y_velo -= 0.05
                self.p1y_velo = round(self.p1y_velo, 2)
            elif self.p1y_velo < 0:
                self.p1y_velo += 0.05
                self.p1y_velo = round(self.p1y_velo, 2)
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            if not self.slowdown1x:
                self.slowdown1x = True
                self.x1_start_ticks = pygame.time.get_ticks()
            x1_seconds = (pygame.time.get_ticks() - self.x1_start_ticks)/1000
            if x1_seconds > 1:
                self.p1x_velo = 0
            if self.p1x_velo > 0:
                self.p1x_velo -= 0.05
                self.p1x_velo = round(self.p1x_velo, 2)
            elif self.p1x_velo < 0:
                self.p1x_velo += 0.05
                self.p1x_velo = round(self.p1x_velo, 2)
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            if not self.slowdown2y:
                self.slowdown2y = True
                self.y2_start_ticks = pygame.time.get_ticks()
            y2_seconds = (pygame.time.get_ticks() - self.y2_start_ticks)/1000
            if y2_seconds > 1:
                self.p2y_velo = 0
            if self.p2y_velo > 0:
                self.p2y_velo -= 0.05
                self.p2y_velo = round(self.p2y_velo, 2)
            elif self.p2y_velo < 0:
                self.p2y_velo += 0.05
                self.p2y_velo = round(self.p2y_velo, 2)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if not self.slowdown2x:
                self.slowdown2x = True
                self.x2_start_ticks = pygame.time.get_ticks()
            x2_seconds = (pygame.time.get_ticks() - self.x2_start_ticks)/1000
            if x2_seconds > 1:
                self.p2x_velo = 0
            if self.p2x_velo > 0:
                self.p2x_velo -= 0.05
                self.p2x_velo = round(self.p2x_velo, 2)
            elif self.p2x_velo < 0:
                self.p2x_velo += 0.05
                self.p2x_velo = round(self.p2x_velo, 2)

        if self.p1y_velo != 0 or self.p1x_velo != 0:
            if self.p1y_velo >= 2 and self.p1x_velo <= 1 and self.p1x_velo >= -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 180)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo <= -2 and self.p1x_velo <= 1 and self.p1x_velo >= -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 0)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1x_velo >= 2 and self.p1y_velo <= 1 and self.p1y_velo >= -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 270)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1x_velo <= -2 and self.p1y_velo <= 1 and self.p1y_velo >= -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 90)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo > 1 and self.p1x_velo > 1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 225)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo < -1 and self.p1x_velo < -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 45)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo < -1 and self.p1x_velo > 1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 315)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo > 1 and self.p1x_velo < -1:
                self.p1rot= pygame.transform.rotate(self.p1_kart, 135)
                p1new_rect = self.p1rot.get_rect(center = self.p1_kart.get_rect(center = (self.player1x+15, self.player1y+15)).center)
        if self.p2y_velo != 0 or self.p2x_velo != 0:
            if self.p2y_velo >= 2 and self.p2x_velo <= 1 and self.p2x_velo >= -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 180)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo <= -2 and self.p2x_velo <= 1 and self.p2x_velo >= -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 0)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2x_velo >= 2 and self.p2y_velo <= 1 and self.p2y_velo >= -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 270)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2x_velo <= -2 and self.p2y_velo <= 1 and self.p2y_velo >= -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 90)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo > 1 and self.p2x_velo > 1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 225)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo < -1 and self.p2x_velo < -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 45)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo < -1 and self.p2x_velo > 1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 315)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo > 1 and self.p2x_velo < -1:
                self.p2rot= pygame.transform.rotate(self.p2_kart, 135)
                p2new_rect = self.p2rot.get_rect(center = self.p2_kart.get_rect(center = (self.player2x+15, self.player2y+15)).center)
        
        if self.player1x <= 0:
            self.player1x = 0
            self.p1x_velo = -self.p1x_velo
        if self.player1x >= 930:
            self.player1x = 930
            self.p1x_velo = -self.p1x_velo
        if self.player1y <= 0:
            self.player1y = 0
            self.p1y_velo = -self.p1y_velo
        if self.player1y >= 690:
            self.player1y = 690
            self.p1y_velo = -self.p1y_velo
        if self.player2x <= 0:
            self.player2x = 0
            self.p2x_velo = -self.p2x_velo
        if self.player2x >= 930:
            self.player2x = 930
            self.p2x_velo = -self.p2x_velo
        if self.player2y <= 0:
            self.player2y = 0
            self.p2y_velo = -self.p2y_velo
        if self.player2y >= 690:
            self.player2y = 690
            self.p2y_velo = -self.p2y_velo

        if kart_collide:
            self.x1_start_ticks = pygame.time.get_ticks()
            self.y1_start_ticks = pygame.time.get_ticks()
            self.x2_start_ticks = pygame.time.get_ticks()
            self.y2_start_ticks = pygame.time.get_ticks()
            switch1x = self.p1x_velo
            switch1y = self.p1y_velo
            switch2x = self.p2x_velo
            switch2y = self.p2y_velo
            self.p1x_velo = switch2x
            self.p1y_velo = switch2y
            self.p2x_velo = switch1x
            self.p2y_velo = switch1y

    def waluigitrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((128, 0, 128))
            kartgame.karts(self)


            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def rainbowtrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((0, 0, 0))
            kartgame.karts(self)


            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def mariotrack(self) -> None:
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            screen.fill((178, 0, 0))
            kartgame.karts(self)


            pygame.display.flip()
            clock.tick(60)
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
            pygame.mixer.music.load("SNES music Super Mario Kart  - Rainbow Road.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            kartgame.rainbowtrack(self)
        else:
            pygame.mixer.music.load("Super Mario Kart Music (SNES) - Mario Circuit.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            kartgame.mariotrack(self)

if __name__ == "__main__":
    game = kartgame()
    game.run()
