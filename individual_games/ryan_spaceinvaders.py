# Game where you control a slime hunter that shoots slimes coming from the top side of the screen. 
# Slimes get progressively harder (different types + difficulty curve)
# You can find better weapons.
# Maybe a boss / bonus levels

# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 1280
HEIGHT = 960
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables



    



ticks = 0

char1_x = 200
char1_y = 200
char1_speed = 5
bullet1_speed = 5
bulletreload1 = 1
bullettype1 = "rocket"

char2_x = 200
char2_y = 200
char2_speed = 5
bullet2_speed = 5
bulletreload2 = 1
bullettype2 = "machine"

bullets1 = [] #format: [x, y, radius, speed, damage]
bullets2 = [] #format: [x, y, radius, speed, damage]


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] == True and char1_x > 0:
        char1_x -= char1_speed
    if keys[pygame.K_d] == True and char1_x < WIDTH:
        char1_x += char1_speed
    if keys[pygame.K_w] == True and char1_y > 0:
        char1_y -= char1_speed
    if keys[pygame.K_s] == True and char1_y < HEIGHT:
        char1_y += char1_speed
    if keys[pygame.K_LEFT] == True and char2_x > 0:
        char2_x -= char2_speed
    if keys[pygame.K_RIGHT] == True and char2_x < WIDTH:
        char2_x += char2_speed
    if keys[pygame.K_UP] == True and char2_y > 0:
        char2_y -= char2_speed
    if keys[pygame.K_DOWN] == True and char2_y < HEIGHT:
        char2_y += char2_speed
                

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    ticks += 1
    bulletreload1 -= 1
    bulletreload2 -= 1


    # DRAWING

    screen.fill((255, 255, 255))

    if bulletreload1 == 0:
        if bullettype1 == "normal":
            bulletreload1 = 20
            bullets1.append([char1_x, char1_y, 10, 15, 1])
        elif bullettype1 == "machine":
            bulletreload1 = 5
            bullets1.append([char1_x, char1_y, 5, 10, 1])
        elif bullettype1 == "shotgun":
            bulletreload1 = 30
            bullets1.append([char1_x, char1_y, 8, 10, 1])
            bullets1.append([char1_x + 10, char1_y, 8, 10, 1, "shotgun1"])
            bullets1.append([char1_x - 10, char1_y, 8, 10, 1, "shotgun2"])
        elif bullettype1 == "rocket":
            bulletreload1 = 40
            bullets1.append([char1_x, char1_y, 20, 5, 1])

    if bulletreload2 == 0:
        if bullettype2 == "normal":
            bulletreload2 = 20
            bullets2.append([char2_x, char2_y, 10, 15, 1])
        elif bullettype2 == "machine":
            bulletreload2 = 5
            bullets2.append([char2_x, char2_y, 5, 20, 1])
        elif bullettype2 == "shotgun":
            bulletreload2 = 30
            bullets2.append([char2_x, char2_y, 8, 10, 1])
            bullets2.append([char2_x + 10, char2_y, 8, 10, 1, "shotgun1"])
            bullets2.append([char2_x - 10, char2_y, 8, 10, 1, "shotgun2"])
        elif bullettype2 == "rocket":
            bulletreload2 = 40
            bullets2.append([char2_x, char2_y, 20, 5, 1])
    

    pygame.draw.circle(screen, (0, 0, 255), (char1_x, char1_y), 30)
    pygame.draw.circle(screen, (0, 255, 0), (char2_x, char2_y), 30)

    for bullet in bullets1:
        pygame.draw.circle(screen, (0, 0, 255), (bullet[0], bullet[1]), bullet[2])
        bullet[1] -= bullet[3]
        try:
            if bullet[5] == "shotgun1":
                bullet[0] += 1
            elif bullet[5] == "shotgun2":
                bullet[0] -= 1
        except IndexError:
            pass
        if bullet[1] < 0 - bullet[2]:
            bullets1.remove(bullet)


    for bullet in bullets2:
        pygame.draw.circle(screen, (0, 255, 0), (bullet[0], bullet[1]), bullet[2])
        bullet[1] -= bullet[3]
        try:
            if bullet[5] == "shotgun1":
                bullet[0] += 1
            elif bullet[5] == "shotgun2":
                bullet[0] -= 1
        except IndexError:
            pass
        if bullet[1] < 0 - bullet[2]:
            bullets2.remove(bullet)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
